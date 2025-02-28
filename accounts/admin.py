from django.contrib import admin
from .froms import CustomerUserChangeForm, CustomerUserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

CustomerUser = get_user_model()

class CustomerUserAdmin(UserAdmin):
    add_form = CustomerUserCreationForm
    model = CustomerUser
    list_display = [
        'email',
        'username',
        'is_superuser'
    ]
    
admin.site.register(CustomerUser, CustomerUserAdmin)
