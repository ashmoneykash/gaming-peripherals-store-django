from django.shortcuts import render, redirect
from .models import User
from adminapp.models import Order

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

    for item in items:
        name = item.name.lower()

        if 'mousepad' in name:
            item.image_path = 'products/mousepad.png'
        elif 'keyboard' in name:
            item.image_path = 'products/keyboard.png'
        elif 'headset' in name:
            item.image_path = 'products/headset.png'
        elif 'controller' in name:
            item.image_path = 'products/controller.png'
        elif 'mouse' in name:
            item.image_path = 'products/mouse.png'
        else:
            item.image_path = 'products/keyboard.png'

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

