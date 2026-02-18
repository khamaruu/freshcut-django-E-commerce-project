from django.shortcuts import render , redirect
from django.contrib.auth import authenticate, login as auto_login, logout as auto_logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
from .models import Category, SubCategory, Product
from .forms import CategoryForm, SubCategoryForm, ProductForm
from django.shortcuts import render, get_object_or_404


def admin_only(user):
    return user.is_authenticated and user.is_staff


# CATEGORY
@user_passes_test(admin_only)
def category_list(request):
    return render(request, "category_list.html", {
        "categories": Category.objects.all()
    })


@user_passes_test(admin_only)
def category_create(request):
    form = CategoryForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("category_list")
    return render(request, "form.html", {"form": form})


# SUBCATEGORY
@user_passes_test(admin_only)
def subcategory_list(request):
    return render(request, "subcategory_list.html", {
        "subcategories": SubCategory.objects.select_related("category")
    })


@user_passes_test(admin_only)
def subcategory_create(request):
    form = SubCategoryForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("subcategory_list")
    return render(request, "form.html", {"form": form})


# PRODUCT
@user_passes_test(admin_only)
def product_list(request):
    return render(request, "product_list.html", {
        "products": Product.objects.select_related("category", "subcategory")
    })


@user_passes_test(admin_only)
def product_create(request):
    form = ProductForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect("product_list")
    return render(request, "form.html", {"form": form})

@user_passes_test(admin_only)
def product_edit(request, slug):
    product = get_object_or_404(Product, slug=slug)

    form = ProductForm(
        request.POST or None,
        request.FILES or None,
        instance=product
    )

    if form.is_valid():
        form.save()
        return redirect("product_list")

    return render(request, "form.html", {
        "form": form,
        "title": "Edit Product"
    })


@user_passes_test(admin_only)
def product_toggle(request, slug):
    product = get_object_or_404(Product, slug=slug)
    product.is_active = not product.is_active
    product.save()
    return redirect("product_list")


def adminlogin(request):
    return render(request,'adminlogin.html')
@login_required
def dashboard(request):
    return render(request, "admindashboard.html")
@login_required
def product(request):
    return render (request,'product.html')
@login_required
def categories(request):
    return render(request,'categories.html')
@login_required
def orders(request):
    return render(request,'orders.html')
@login_required
def customers(request):
    return render(request,'customers.html')
@login_required
def coupons(request):
    return render(request,'coupons.html')
@login_required
def banners(request):
    return render(request,'banners.html')
@login_required
def addproduct(request):
    return render (request,'addproduct.html')
@never_cache
@login_required
def adminlogout(request):
    auto_logout(request)
    return redirect ('login')

