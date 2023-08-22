from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from accounts.decorators import unauthenticated_user, admin_required
from accounts.forms import CreateUserForm, ProductForm, OrderForm
from .models import Product, Cart, Order


# Create your views here.

@admin_required
def admin_dashboard(request):
    products = Product.objects.all()
    orders = Order.objects.all()

    context = {'products': products, 'orders': orders}
    return render(request, 'accounts/admin/admin_dashboard.html', context)


@admin_required
def add_product(request):
    product = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')

    context = {'product': product}
    return render(request, 'accounts/admin/add_product.html', context)


@admin_required
def delete_product(request, pk):
    product = Product.objects.get(id=pk)
    if request.method == "POST":
        product.delete()
        return redirect('admin_dashboard')

    context = {'product': product}
    return render(request, 'accounts/admin/delete_product.html', context)


@admin_required
def ship_order(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == "POST":
        order.shipped = 'shipped'
        order.save()
        return redirect('admin_dashboard')

    context = {'order': order}
    return render(request, 'accounts/admin/ship_order.html', context)


@admin_required
def update_product(request, pk):
    product = Product.objects.get(id=pk)
    form = ProductForm(instance=product)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')

    context = {'product': form}
    return render(request, 'accounts/admin/update_product.html', context)


def home(request):
    return render(request, 'accounts/home.html')


@unauthenticated_user
def sign_up(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect('log_in')

    context = {'form': form}
    return render(request, 'accounts/login-signup/sign_up.html', context)


@unauthenticated_user
def log_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR password is incorrect')
    return render(request, 'accounts/login-signup/log_in.html')


@login_required(login_url='log_in')
def logout_user(request):
    logout(request)
    return redirect('home')


def shop(request):
    products = Product.objects.all()

    context = {'products': products}
    return render(request, 'accounts/shop_related/shop.html', context)


@login_required(login_url='log_in')
def cart(request):
    current_cart = None
    total = 0

    form = OrderForm()
    if Cart.objects.filter(user=request.user).exists():
        current_cart = Cart.objects.get(user=request.user)
        for item in current_cart.items.all():
            total += item.price

    context = {'cart': current_cart, 'total': total, 'form': form}
    return render(request, 'accounts/cart_related/cart.html', context)


@login_required(login_url='log_in')
def checkout(request):
    current_cart = None
    total = 0

    form = OrderForm()
    if Cart.objects.filter(user=request.user).exists():
        current_cart = Cart.objects.get(user=request.user)
        for item in current_cart.items.all():
            total += item.price

    if request.method == 'POST':
        form = OrderForm(request.POST)
        current_cart = Cart.objects.get(user=request.user)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.shipped = 'In Delivery'
            order.save()
            for item in current_cart.items.all():
                order.items.add(item)

                product = Product.objects.get(id=item.id)
                product.quantity -= 1
                product.save()

            current_cart.delete()
            order.save()
            return redirect('home')

    context = {'cart': current_cart, 'total': total, 'form': form}
    return render(request, 'accounts/cart_related/checkout.html', context)


@login_required(login_url='log_in')
def remove_product(request, pk):
    current_cart = Cart.objects.get(user=request.user)
    product = current_cart.items.all().get(id=pk)

    if request.method == "POST":
        current_cart.items.remove(product)
        if not current_cart.items.all().exists():
            current_cart.delete()
        return redirect('cart')

    context = {'product': product}
    return render(request, 'accounts/cart_related/remove_from_cart.html', context)


def view_product(request, pk):
    product = Product.objects.get(id=pk)
    if request.method == 'POST':
        if request.user.is_authenticated:
            if not Cart.objects.filter(user=request.user).exists():
                Cart.objects.create(
                    user=request.user,
                )

            current_cart = Cart.objects.get(user=request.user)
            current_cart.items.add(product)
            current_cart.save()
            return redirect('shop')
        else:
            return redirect('log_in')

    context = {'product': product}
    return render(request, 'accounts/shop_related/view_product.html', context)
