from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from .models import Contact
from math import ceil
# Create your views here.


def index(request):
    allProds = []
    catprods = Product.objects.values('catagory', 'id')
    cats = {item['catagory'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(catagory=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])

    params = {'allProds':allProds}
    return render(request, "shop/index.html", params)

def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
    return render(request, 'shop/contact.html')

def productView(request, myid):
    # Fetch the product using the id
    product = Product.objects.filter(id=myid)


    return render(request, 'shop/prodView.html', {'product':product[0]})
