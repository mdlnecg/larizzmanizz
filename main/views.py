from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name' : 'Chocolate CoKIEZZ',
        'price': '10.000',
        'description': 'The only cooKIEZZ that brings happiNEZZ!'
    }

    return render(request, "main.html", context)