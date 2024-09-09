from django.shortcuts import render

def show_main(request):
    products = [
        {
            'name': 'Chocolate CooKIEZZ',
            'description': 'Delicious chocolate cookie with a gooey center.',
            'price': 10.000,
            'image_url': '"C:\Users\Madeline\Documents\pacil\TERM 3\PBP\PICTS\chocoKIEZZ.jpg"'
        },
        {
            'name': 'Peanut Butter Cookie',
            'description': 'Rich peanut butter cookie with a crunchy exterior.',
            'price': 18000,
            'image_url': '"C:\Users\Madeline\Documents\pacil\TERM 3\PBP\PICTS\RVKIEZZ.jpg"'
        },
        # Tambahkan produk lainnya
    ]

    context = {
        'name': 'LaRizzManizz',
        'shop_at': 'Your Favorite Online Cookie Store',
        'products': products,
    }

    return render(request, 'main.html', context)
