from django.contrib import admin
from .models import Comment

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'flagged', 'flag_reason', 'created_at')
    list_filter = ('flagged', 'created_at')
    search_fields = ('user__username', 'content')
