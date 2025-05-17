from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index),
    path('novo/', views.novo_post, name='novo_post'),
    re_path(r'^post/(?P<slug>[^\.]+)\.html$', views.ver_post, name='ver_post_blog'),
    re_path(r'^categoria/(?P<slug>[^\.]+)\.html$', views.ver_categoria, name='ver_categoria_blog'),
]