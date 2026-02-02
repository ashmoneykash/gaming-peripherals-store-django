from django.shortcuts import render, redirect
from .models import User
from adminapp.models import Order

IMAGE_MAP = {
    'mousepad': 'products/mousepad.png',
    'keyboard': 'products/keyboard.png',
    'headset': 'products/headset.png',
    'controller': 'products/controller.png',
    'mouse': 'products/mouse.png',
}

def register(request):
    if request.method == 'POST':
        User.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            mobile=request.POST['mobile'],
            password=request.POST['password'],
            address=request.POST['address'],
            pincode=request.POST['pincode']
        )
        return redirect('/login/')
    return render(request, 'registration.html')

def login(request):
    if request.method == 'POST':
        user = User.objects.filter(
            email=request.POST['email'],
            password=request.POST['password']
        ).first()

        if user:
            request.session['user_id'] = user.id
            request.session['user_name'] = user.name
            return redirect('/home/')
    return render(request, 'login.html')

from adminapp.models import Product

def products(request):
    items = Product.objects.all()

    # ── Sorting (ALWAYS before looping)
    sort = request.GET.get('sort')

    if sort == 'name':
        items = items.order_by('name')
    elif sort == 'price-asc':
        items = items.order_by('price')
    elif sort == 'price-desc':
        items = items.order_by('-price')

    # ── Attach image paths (presentation logic only)
    for item in items:
        name = item.name.lower()
        item.image_path = 'products/keyboard.png'  # default fallback

        for keyword, path in IMAGE_MAP.items():
            if keyword in name:
                item.image_path = path
                break

    return render(request, 'users/products.html', {'items': items})

def place_order(request, pid):
    Order.objects.create(
        user_id=request.session['user_id'],
        product_id=pid,
        quantity=1
    )
    return redirect('/my-orders/')

def my_orders(request):
    orders = Order.objects.filter(user_id=request.session['user_id'])
    return render(request, 'my_orders.html', {'orders': orders})

