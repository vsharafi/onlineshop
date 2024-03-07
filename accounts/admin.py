from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserChangeForm, CustomUserCreationForm


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    # fieldsets = CustomUserChangeForm.Meta.fields
    # add_fieldsets = CustomUserCreationForm.Meta.fields
    list_display = ('username', 'email', )

# admin.site.register(CustomUser, CustomUserAdmin)
