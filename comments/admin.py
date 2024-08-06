from django.contrib import admin
from comments.models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'comment_text', 'created_by', 'publication', 'created_at', 'updated_at']
    list_filter = ['id', 'created_by__username', 'publication__title', 'created_at',]
    date_hierarchy = 'created_at'
    search_fields = ['id', 'created_by__username', 'publication__title', 'comment_text']