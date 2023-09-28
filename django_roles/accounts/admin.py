from django.contrib import admin
from .models import Profile  



class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'image', 'address', 'location', 'telephone', 'add_user_group')
    search_fields = ('location', 'user__username', 'user__groups__name')
    list_filter = ['location']
    
    def add_user_group(self, obj):
        return " -- ".join([group.name for group in obj.user.groups.all().order_by('name')])
    
    add_user_group.short_description = 'Grupo'

admin.site.register(Profile, ProfileAdmin)