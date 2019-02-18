
from datetime import date

from django.contrib import admin
from django.contrib.auth.admin import User, UserAdmin

from .models import Profile

admin.site.unregister(User)
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)

# admin.site.unregister(User)
# admin.site.register(User, CustomUserAdmin)

# @admin.register(Profile)
# class ProfileAdmin(admin.ModelAdmin):
# 	list_display = ('address','dob','mobile','country','gender','profession')
# 	list_display_links = ('address','mobile')
# 	list_editable = ('dob','country')
# 	list_filter = ('gender',)
# 	search_fields = ('address','mobile','profession')

# 	def get_age(self, instance): # self ma profileadmin ko aauxa and instance ma profile ko aauxa
# 		age = date.today() - instance.dob
# 		return int(age.days//365.25)

# 	get_age.short_description = 'Age'
# admin.site.register(Profile, ProfileAdmin) #old way


# class ProfileAdmin(admin.ModelAdmin):
# 	list_display = ('address','dob','mobile','country','gender','profession')


# admin.site.register(Profile)
