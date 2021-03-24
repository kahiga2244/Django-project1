from django.contrib import admin
from .models import User,Poll

class UserAdmin(admin.ModelAdmin):
    filter_horizontal =('user',)

admin.site.register(User)
admin.site.register(Poll)

