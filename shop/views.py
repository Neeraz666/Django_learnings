from django.shortcuts import render
from .models import Product, Contact, Order
from math import ceil

# Create your views here.
from django.http import HttpResponse

def index(request):
    allProds = []
    catProds = Product.objects.values('category')
    cats = {item['category'] for item in catProds}
    for cat in cats:
        prod = Product.objects.filter(category = cat)
        n = len(prod)
        nSlides = n//4 + ceil((n/4)-(n//4))
        allProds.append([prod, range(1, nSlides), nSlides])

    params = {'allProds': allProds}
    return render(request, 'shop/index.html', params)

def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
    
    return render(request, 'shop/contact.html')

def tracker(request):
    return HttpResponse("We are at tracker")

def search(request):
    return HttpResponse("We are at search")

def prodView(request, myid):

    product = Product.objects.filter(id = myid)
    return render(request, 'shop/productview.html', {'product' : product[0]})

def checkout(request):
    if request.method == "POST":
        itemsJson = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address', '')
        address_2 = request.POST.get('address_2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip = request.POST.get('zip', '')
        phone = request.POST.get('phone', '')
        orders = Order(itemsJson = itemsJson , name=name, email=email, address=address, address_2=address_2, city=city, state=state, zip=zip, phone=phone)
        orders.save()

        done = True
        id = Order.order_id
        return render(request, 'shop/checkout.html', {'done' : done, 'id' : id})

    return render(request, 'shop/checkout.html')

