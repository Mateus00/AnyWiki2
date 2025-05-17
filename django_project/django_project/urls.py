from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.contrib.sitemaps import Sitemap

from blog.models import Blog
from . import views

# Sitemap para os posts do blog
class BlogSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Blog.objects.all()

    def location(self, item):
        return item.get_url_absoluta()

sitemaps = {
    'blog': BlogSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage),
    path('posts/', views.posts),
    path('sobre/', views.sobre),
    path('blog/', include('blog.urls')),
    path('loja/', include('loja.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('google39cdce1ef57976f4.html', TemplateView.as_view(template_name='google39cdce1ef57976f4.html', content_type='text/html')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
