from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name' : 'Niki Zefanya',
        'shop_at': 'LaRizzManizz',
        'products': 'Glasses'
    }

    return render(request, "main.html", context)