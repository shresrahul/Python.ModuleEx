from django.contrib import admin

# Register your models here.
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
	list_display = ('address','dob','mobile','country','gender','profession')
	list_display_links = ('address','mobile')
	list_editable = ('dob','country')
	list_filter = ('gender',)
	search_fields = ('address','mobile','profession')

# admin.site.register(Profile, ProfileAdmin) #old way


# class ProfileAdmin(admin.ModelAdmin):
# 	list_display = ('address','dob','mobile','country','gender','profession')


# admin.site.register(Profile)