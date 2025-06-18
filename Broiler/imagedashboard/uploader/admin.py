from django.contrib import admin
from .models import UserProfile, ImageUpload
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'mobile')
    search_fields = ('user__username', 'mobile')
class ImageUploadAdmin(admin.ModelAdmin):
    list_display = ('user', 'image', 'uploaded_at')
    list_filter = ('user', 'uploaded_at')
    search_fields = ('user__username',)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(ImageUpload, ImageUploadAdmin)