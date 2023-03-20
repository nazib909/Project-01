from django.shortcuts import render, redirect
from app.models import *
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Q


# Create your views here.

def product(request, id):
    p = Product.objects.get(id=id)

    return render(request, 'product.html', locals())


def add_to_cart(request, id):
    user = request.user

    if user.is_authenticated:
        prod = Product.objects.get(id=id)
        if prod:
            if Cart.objects.filter(Q(user=user) & Q(product=prod)).exists():
                messages.error(request, 'Product allready exist in your cart.')
            else:
                a = Cart(user=user, product=prod).save()

    cc = Cart.objects.filter(user=user).count()
    return redirect('home')


def cart(request):
    user = request.user
    cc = Cart.objects.filter(user=user).count()
    cart_prod = Cart.objects.filter(user=user)
    if cart_prod:
        total = 0.00
        amount = 0.00
        shipping = 1
        cartProduct = [p for p in Cart.objects.all() if p.user == user]
        if cartProduct:
            for p in cartProduct:
                tempAmount = (p.quantity)*(p.product.price)
                amount = amount + tempAmount
                totalAmountShipping = amount + shipping

    remov = request.GET.get('remove')
    if remov:
        a = Cart.objects.get(user = user , product = remov)
        a.delete()
        return redirect('cart')


    return render(request, 'Cart.html', locals())
