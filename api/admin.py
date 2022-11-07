from django.contrib import admin

from .models import Domain, RememberedUsername

admin.site.register(Domain)
admin.site.register(RememberedUsername)
