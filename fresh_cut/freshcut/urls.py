from django.contrib import admin
from django.urls import path
from freshcut import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.freshcut, name='freshcut'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('placeorder/', views.placeorder, name='placeorder'),
    path('successorder/', views.successorder, name='successorder'),
    path('fish/', views.fish, name='fish'),
    path('chicken/', views.chicken, name='chicken'),
    path('mutton/', views.mutton, name='mutton'),
    path('beef/', views.beef, name='beef'),
    path('myorder/', views.myorder, name='myorder'),
    path('profile/', views.profile, name='profile'),
    path("product_detail/<slug:slug>/", views.product_detail, name="product_detail"),
    path("search/", views.product_search, name="product_search"),
    path("remove/<int:item_id>/", views.remove_cart_item, name="remove_cart_item"),
    path("update-cart/<int:item_id>/",views.update_cart_quantity,name="update_cart_quantity"),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path("place-order/", views.placeorder, name="placeorder"),
    path("order/<int:order_id>/", views.order_detail, name="order_detail"),
    path("add-address/", views.add_address, name="add_address"),
    path("create-order/", views.create_order, name="create_order"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )