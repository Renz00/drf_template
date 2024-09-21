from django.contrib import admin
from django.urls import path
from drf import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # Drink CRUD routes
    path('drinks/get', views.get),
    path('drinks/store', views.store),
    path('drinks/show/<int:id>', views.show),
    path('drinks/update/<int:id>', views.update),
    path('drinks/delete/<int:id>', views.delete),
]
