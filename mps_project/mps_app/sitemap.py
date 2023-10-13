from django.contrib.sitemaps import Sitemap
from .models import Prompts


class PostSiteMap(Sitemap) :
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Prompts.objects.filter(status="published")
    
    def lastmod(self,obj):
        return obj.updated
    
class HomeSiteMap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9



    def items(self):
        return [
            '/',
            '/login/',
            '/signup/',
            '/affiliate/',

        ]
    def location(self,obj):
        return obj

