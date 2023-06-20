from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, "chollo_main/index.html")


def product(request):
    return render(request, "chollo_main/product.html")


def signin(request):
    return render(request, "chollo_main/signin.html")


def signup(request):
    return render(request, "chollo_main/signup.html")


def cart_details(request):
    return render(request, "chollo_main/cart-details.html")
