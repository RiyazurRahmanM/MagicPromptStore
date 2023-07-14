from django.urls import path
from . import views
from django.conf import settings 
from django.conf.urls.static import static
urlpatterns = [
    path('',views.home_view,name="home_view"),
    path('store',views.store_view,name='store_view'),
    path('payment',views.payment_view,name="payment_view"),
    path('login/',views.login_view,name="login_view"),
    path('signup/',views.signup_view,name="signup_view"),
    path('post/',views.post_view,name="post_view"),
    path('prompt/',views.prompt_view,name="prompt_view"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)