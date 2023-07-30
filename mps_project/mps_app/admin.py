from django.contrib import admin
from .models import Prompts, Payment, Users, Delivery, Withdraw
# Register your models here.

admin.site.register(Prompts)
admin.site.register(Payment)
admin.site.register(Users)
admin.site.register(Delivery)
admin.site.register(Withdraw)