<<<<<<< HEAD
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core import serializers
from .models import Product
from main.forms import ProductEntryForm

# Create your views here.
def show_model(request):
    model = Product.objects.all()

=======
from django.shortcuts import render
from .models import Product

# Create your views here.
def show_main(request):
    # Menggunakan data produk dari context (sementara hardcoded)
>>>>>>> 65c6553ca8fcd7cdd99e145cf0c3d98d1e605d7b
    context = {
        'name' : 'Madeline Clairine Gultom',
        'npm' : '2306207846',
        'class' : 'PBP D',
<<<<<<< HEAD
        'products': model,
    }

    return render(request, "main.html", context)

def create_product_form(request):
    form = ProductEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_model')

    context = {'form': form}
    return render(request, 'create_product.html', context)

def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
=======
        'products': [
            {
                'name': 'Chocolate CoKIEZZ',
                'price': '10.000',
                'description': 'The only cooKIEZZ that brings happiNEZZ!',
                'rating': '⭐⭐⭐⭐⭐',
            },
            {
                'name': 'Red Velvet CoKIEZZ',
                'price': '12.000',
                'description': 'A KIEZZ from 7th Heaven!',
                'rating': '⭐⭐⭐⭐',
            },
            {
                'name': 'Oreo CoKIEZZ',
                'price': '10.000',
                'description': 'RUN from skibidi, GET your Oreozzz!!',
                'rating': '⭐⭐⭐⭐',
            }
        ]
    }

    return render(request, "main.html", context)
>>>>>>> 65c6553ca8fcd7cdd99e145cf0c3d98d1e605d7b
