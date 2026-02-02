from django.shortcuts import *
from adminapp.models import Product,Order
from django.db.models import Sum, F

# Create your views here.
def add_product(request):
    if request.method == 'POST':
        Product.objects.create(
            name=request.POST['name'],
            price=request.POST['price'],
            description=request.POST['description'],
            stock=request.POST['stock']
        )
        return redirect('/adminapp/')
    return render(request, 'adminapp/add_product.html')

def view_orders(request):
    orders = Order.objects.all()
    return render(request, 'orders.html', {'orders': orders})

def sales_report(request):
    report = Order.objects.aggregate(
        total_sales=Sum(F('quantity') * F('product__price'))
    )
    return render(request, 'sales.html', {'report': report})
