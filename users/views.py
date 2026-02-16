from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from adminapp.models import Order,Product
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from .models import UserProfile

IMAGE_MAP = {
    'mousepad': 'products/mousepad.png',
    'keyboard': 'products/keyboard.png',
    'headset': 'products/headset.png',
    'controller': 'products/controller.png',
    'mouse': 'products/mouse.png',
}

def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if password1 != password2:
            return render(request, "users/register.html", {
                "error": "Passwords do not match"
            })

        if User.objects.filter(username=username).exists():
            return render(request, "users/register.html", {
                "error": "Username already exists"
            })

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password1
        )

        UserProfile.objects.create(user=user)
        return redirect("login")

    return render(request, "users/register.html")

def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            django_login(request, user)
            return redirect("products")
        else:
            return render(request, "users/login.html", {
                "error": "Invalid username or password"
            })

    return render(request, "users/login.html")

def products(request):
    items = Product.objects.all()

    # ── Sorting (ALWAYS before looping)
    sort = request.GET.get('sort','')

    if sort == 'name':
        items = items.order_by('name')
    elif sort == 'price-asc':
        items = items.order_by('price')
    elif sort == 'price-desc':
        items = items.order_by('-price')

    # ── Attach image paths (presentation logic only)
    for item in items:
        name = item.name.lower()
        item.image_path = 'products/keyboard.png'

        for keyword in sorted(IMAGE_MAP.keys(), key=len, reverse=True):
            if keyword in name:
                item.image_path = IMAGE_MAP[keyword]
                break

    return render(request, 'users/products.html', {'products': items})

@login_required(login_url='/users/login/')
def buy_product(request, product_id):
    if request.method != "POST":
        return redirect('products')

    product = get_object_or_404(Product, id=product_id)

    if product.stock <= 0:
        return redirect('products')

    Order.objects.create(
        user=request.user,
        product=product,
        quantity=1
    )

    product.stock -= 1
    product.save()

    return redirect('my_orders')

@login_required(login_url='/users/login/')
def my_orders(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'users/my_orders.html', {'orders': orders})

def logout(request):
    django_logout(request)
    return redirect("home")

