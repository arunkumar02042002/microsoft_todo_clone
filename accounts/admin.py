from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = [
    "email",
    "username",
    "bio",
    "is_staff",
    ]
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("bio", "profile_img")}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("bio", "profile_img")}),)

admin.site.register(User, CustomUserAdmin)