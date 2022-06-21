from django.contrib import admin
from .models import Post, Meme, Project
# Register your models here.

class PostAdminDashboard(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ('status',)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

class MemeAdminDashboard(admin.ModelAdmin):
    list_display = ('title', 'slug', 'image', 'updated_on')
    list_filter = ('status',)   
    search_fields = ['title']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Post, PostAdminDashboard)
admin.site.register(Meme)
admin.site.register(Project)
