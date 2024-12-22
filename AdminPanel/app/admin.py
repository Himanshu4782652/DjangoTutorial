from django.contrib import admin
from .models import * #now, we can access all models that was created in models.py

# Register your models here.
admin.site.register(Teacher)