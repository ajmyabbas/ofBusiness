from unicodedata import name
from django import views
from django.urls import include, path
from.import views

urlpatterns = [

    path('',views.index,name='index'),
    path('categories/',views.categories,name='categories'),
    path('products/',views.products,name='products'),
    path('mycart/',views.mycart,name='mycart'),

]