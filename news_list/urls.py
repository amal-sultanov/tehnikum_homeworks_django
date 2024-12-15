from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage),
    path('news/<int:pk>', views.news_page),
    path('category/<int:pk>', views.category_page),
    path('register', views.Register.as_view()),
    path('logout', views.logout_view),
    path('add-to-wishlist/<int:pk>', views.add_to_wishlist),
    path('delete-from-wishlist/<int:pk>', views.delete_from_wishlist),
    path('wishlist', views.wishlist_page),
]
