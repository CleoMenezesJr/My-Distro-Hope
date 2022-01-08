from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login_view'),
    path('register/', views.register_view, name='register_view'),
    path('add_blog/', views.add_blog, name='add_blog'),
    path('blog-detail/<slug>', views.blog_detail, name='blog_detail'),
    path('see-blogs/', views.see_blogs, name='see_blogs'),
    path('blog_delete/<id>', views.blog_delete, name='blog_delete'),
    path('blog_update/<slug>', views.blog_update, name='blog_update'),
    path('logout_view/', views.logout_view, name='logout_view'),
    path('virify/<token>/', views.verify, name='verify'),
    path('theme', views.theme, name='theme')
]
