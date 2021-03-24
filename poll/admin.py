from django.contrib import admin
from .models import User,Poll,Commentor


admin.site.register(Commentor)
admin.site.register(User)
admin.site.register(Poll)

