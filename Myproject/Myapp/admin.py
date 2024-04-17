from django.contrib import admin # type: ignore

#register your models her
from .models import User
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
      list_display = ['id', 'email', 'first_name','first_name', 'password', 'username'
]