from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Comment, User, FlaggedComment, Review,FlaggedReview

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    model = User
    list_display = ('email', 'username', 'is_staff')
    ordering = ('email',)
    fieldsets = BaseUserAdmin.fieldsets

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'flagged', 'flag_reason', 'created_at')
    list_filter = ('flagged', 'created_at')
    search_fields = ('user__email', 'content')

@admin.register(FlaggedComment)
class FlaggedCommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'reason', 'created_at')
    search_fields = ('user__email', 'content')
    list_filter = ('created_at',)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'flagged', 'flag_reason', 'created_at')
    list_filter = ('flagged', 'created_at')
    search_fields = ('user__email', 'content')

@admin.register(FlaggedReview)
class FlaggedReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'reason', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('user__email', 'content')