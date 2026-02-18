# from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Django default admin
    # path('admin/', admin.site.urls),

    # User site
    path('', include('freshcut.urls')),

    # Custom admin panel
    path('', include('adminpage.urls')),
]
