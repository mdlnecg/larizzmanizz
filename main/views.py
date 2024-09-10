from django.shortcuts import render
from .models import Product

# Create your views here.
def show_main(request):
    # Menggunakan data produk dari context (sementara hardcoded)
    context = {
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
