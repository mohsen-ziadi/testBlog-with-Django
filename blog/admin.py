from django.contrib import admin
from .models import Post,Account

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','slug','author','publish','status')
    list_filter = ('status', 'publish', 'created','author')
    search_field =('title','body')
    date_hierarchy = 'publish'
    ordering = ('-publish','status')
    list_editable =('status',)
    list_display_links = ('slug',)

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('gender',)
