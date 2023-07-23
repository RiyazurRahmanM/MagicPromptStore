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
    path('seeprompt/',views.seeprompt_view,name="seeprompt_view"),
    path('agreement/',views.agreement_view,name="agreement_view"),
    path('post_form/',views.post_form_view,name="post_form_view"),
    path('process/',views.process_view,name="process_view"),
    path('my_prompts/',views.my_prompts_view,name="my_prompts_view"),
    path('delivery/',views.delivery_view,name="delivery_view"),
    path('delivery_form/',views.delivery_form_view,name="delivery_form_view"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)