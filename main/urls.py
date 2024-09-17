from django.urls import path
<<<<<<< HEAD
from main.views import show_model, create_product_form, show_xml, show_json, show_xml_by_id, show_json_by_id
=======
from main.views import show_main
>>>>>>> 65c6553ca8fcd7cdd99e145cf0c3d98d1e605d7b

app_name = 'main'

urlpatterns = [
<<<<<<< HEAD
    path('', show_model, name='show_model'),
    path('create-product-form/', create_product_form, name='create_product_form'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
=======
    path('', show_main, name='show_main'),
>>>>>>> 65c6553ca8fcd7cdd99e145cf0c3d98d1e605d7b
]