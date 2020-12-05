from django.urls import path
from .views import  PostListView
   
from . import views

urlpatterns = [
        path('payment/', views.payment, name='payment'),

    path('main/', views.main, name='home-main'),
    path('post_order/', views.post_order, name='post_order'),
    path('home-home/', PostListView.as_view(), name='home-home'),
        path('', views.home, name='home'),
            path('home2', views.home2, name='home2'),
        path('order_bid', views.order_bid, name='order_bid'),

#    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('contact/', views.contact, name='home-contact'),
    
]
