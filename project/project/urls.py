from django.urls import path
from bookstore import views
from django.urls import path, include
from rest_framework import routers
from bookstore import views

router = routers.DefaultRouter()
router.register(r'books', views.BookViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
    path('books/', views.book_list, name='book_list'),
    path('books/add/', views.add_book, name='add_book'),
    path('books/add_to_cart/<int:book_id>/', views.add_to_cart, name='add_to_cart'),
]
