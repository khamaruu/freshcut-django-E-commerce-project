from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auto_login, logout as auto_logout
from .forms import SignupForm, LoginForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from adminpage.models import Product, Category
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Cart
def freshcut(request):
    return render(request, 'home.html')

@never_cache
def login_view(request):
    if request.user.is_authenticated:
        return redirect('freshcut')

    form = LoginForm(request.POST)

    if request.method == 'POST' and form.is_valid():
        user = authenticate(
            request,
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password']
        )

        

        if user is not None:
            auto_login(request, user)  
           
            if user.is_staff or user.is_superuser:
                return redirect('dashboard')  
            return redirect('freshcut')
        else:
            form.add_error(None, "Invalid username or password")

          

    return render(request, 'login.html', {'form': form})


def signup(request):
    form = SignupForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('login')

    return render(request, 'signup.html', {'form': form})

@never_cache
def logout_view(request):
    auto_logout(request)
    return redirect('login')


@login_required
def checkout(request): 
    return render(request, 'checkout.html')

@login_required
def placeorder(request): 
    return render(request, 'placeorder.html')

@login_required
def successorder(request): 
    return render(request, 'successorder.html')


def fish(request):
    category = Category.objects.get(name__iexact="Fish")

    products = Product.objects.filter(
        category=category,
        is_active=True
    )

    return render(request, "fish.html", {
        "products": products
    })


def chicken(request):
    category = Category.objects.get(name__iexact="Chicken")
    products = Product.objects.filter(category=category, is_active=True)
    return render(request, "chicken.html", {"products": products})


def mutton(request):
    category =  Category.objects.get(name__iexact="mutton")
    products = Product.objects.filter(category=category, is_active=True)
    return render(request, 'mutton.html',{'products': products} )



def beef(request):
    category=Category.objects.get(name__iexact="beef")
    products=Product.objects.filter(category=category,is_active=True)
    return render(request, 'beef.html',{'products':products})

@login_required
def myorder(request): 
    return render(request, 'myorder.html')

@login_required
def profile(request):
    return render(request, 'profile.html')

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)

    cart_product_ids = []

    if request.user.is_authenticated:
        cart_product_ids = list(Cart.objects.filter(user=request.user).values_list("product_id", flat=True))


    context = {
        "product": product,
        "cart_product_ids": cart_product_ids
    }
    return render(request, "detailproduct.html", context)

def product_search(request):
    query = request.GET.get("q", "").strip()

    if query:
        products = Product.objects.filter(
            name__icontains=query,
            is_active=True
        )
    else:
        products = Product.objects.none()

    return render(request, "product_search.html", {
        "products": products,
        "query": query,
    })


@login_required
def cart(request):
    if request.method == "POST":
        product_id = request.POST.get("product_id")
        product = get_object_or_404(Product, id=product_id)
        cart_item, created = Cart.objects.get_or_create(user=request.user,product=product)

        if not created:
            cart_item.quantity += 1
            cart_item.save()

        return redirect(request.META.get("HTTP_REFERER", "cart"))

    cart_items = Cart.objects.filter(user=request.user)
    subtotal = sum(item.subtotal for item in cart_items)
    total_items = sum(item.quantity for item in cart_items)


    return render(request, "cart.html", {
        "cart_items": cart_items,
        "subtotal": subtotal,
        "total_items":total_items,
    })


@login_required
def update_cart_quantity(request, item_id):
    item = get_object_or_404(Cart, id=item_id, user=request.user)

    if request.method == "POST":
        action = request.POST.get("action")

        if action == "increase":
            item.quantity += 1

        elif action == "decrease":
            item.quantity -= 1
            if item.quantity <= 0:
                item.delete()
                return redirect("cart")

        item.save()

    return redirect("cart")
    
@login_required
def remove_cart_item(request, item_id):
    cart_item = get_object_or_404(Cart, id=item_id, user=request.user)
    cart_item.delete()
    return redirect("cart")