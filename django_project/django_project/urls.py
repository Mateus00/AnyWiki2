from django.contrib import admin
from django.urls import path, include, reverse
from django.views.generic import TemplateView
from django.contrib.sitemaps.views import sitemap
from django.contrib.sitemaps import Sitemap
from django.conf import settings
from django.conf.urls.static import static

from blog.models import Blog
from . import views

# Sitemap para posts do blog
class BlogSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Blog.objects.all()

    def location(self, item):
        return item.get_url_absoluta()

# Sitemap para páginas estáticas
class StaticViewSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5

    def items(self):
        return ['homepage', 'posts', 'sobre']

    def location(self, item):
        return reverse(item)

sitemaps = {
    'static': StaticViewSitemap,
    'blog': BlogSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='homepage'),
    path('posts/', views.posts, name='posts'),
    path('sobre/', views.sobre, name='sobre'),
    path('blog/', include('blog.urls')),
    path('loja/', include('loja.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
    path('google39cdce1ef57976f4.html', TemplateView.as_view(template_name='google39cdce1ef57976f4.html', content_type='text/html')),
]

# Servir mídia e estáticos (em desenvolvimento)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
