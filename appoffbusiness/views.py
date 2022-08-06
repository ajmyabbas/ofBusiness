from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def categories(request):
    return render(request,'categories.html')    

def products(request):
    return render(request,'products.html') 

def mycart(request):
    return render(request,'mycart.html') 