from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.forms import CustomUseChangeForm, CustomUseCreationForm
from accounts.models import CustomUser

# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form= CustomUseCreationForm
    form= CustomUseChangeForm
    model= CustomUser
    list_display=[
        'email',
        'username',
        'age',
        'is_staff',
    ]
    fieldsets = UserAdmin.fieldsets  +((None, {"fields": ("age",)}),)
    add_fieldsets = UserAdmin.add_fieldsets +((None, {"fields": ("age,")}),)

admin.site.register(CustomUser,CustomUserAdmin)
    
    
    
