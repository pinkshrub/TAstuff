from django.contrib import admin
from .models import Lead

# Register your models here.
@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
	pass