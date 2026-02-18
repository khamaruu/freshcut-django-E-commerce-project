from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [

    # =============================
    # AUTH
    # =============================
    path('adminlogin/', views.adminlogin, name='adminlogin'),
    path('adminlogout/', views.adminlogout, name='adminlogout'),


    # =============================
    # DASHBOARD PAGES
    # =============================
    path('dashboard/', views.dashboard, name='dashboard'),
    path('orders/', views.orders, name='orders'),
    path('customers/', views.customers, name='customers'),
    path('coupons/', views.coupons, name='coupons'),
    path('banners/', views.banners, name='banners'),


    # =============================
    # CATEGORY CRUD
    # =============================
    path('categories/', views.category_list, name='category_list'),
    path('categories/add/', views.category_create, name='category_create'),
    # path('categories/<int:pk>/edit/', views.category_update, name='category_update'),


    # =============================
    # SUBCATEGORY CRUD
    # =============================
    path('subcategories/', views.subcategory_list, name='subcategory_list'),
    path('subcategories/add/', views.subcategory_create, name='subcategory_create'),


    # =============================
    # PRODUCT CRUD
    # =============================
    path('products/', views.product_list, name='product_list'),
    path('products/add/', views.product_create, name='product_create'),
    path("product/edit/<slug:slug>/", views.product_edit, name="product_edit"),
    path("product/toggle/<slug:slug>/", views.product_toggle, name="product_toggle"),
]
    # path('products/<int:pk>/edit/', views.product_update, name='product_update'),



# =============================
# MEDIA FILES (images)
# =============================
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
