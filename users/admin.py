from django.contrib import admin

# Register your models here.
from users.models import Identity

admin.site.register(Identity)