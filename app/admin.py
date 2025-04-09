from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from app.models import Article, UserProfile

class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {
            'classes': ('collapse',),
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
        }),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1','password2')
        }),
    )
    list_display = ('email', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    search_fields = ('email',)
    ordering = ('email',)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'word_count', 'status', 'created_at', 'updated_at')
    list_filter = ('status',)
    search_fields = ('title', 'content')
    date_hierarchy = 'created_at'
    ordering = ('created_at',)
    readonly_fields = ('word_count', 'created_at', 'updated_at')

admin.site.register(Article, ArticleAdmin)
admin.site.register(UserProfile, CustomUserAdmin)


