from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from life.models import Comment, NewLifeManagementMember


@admin.register(NewLifeManagementMember)
class NewLifeManagementMemberAdmin(TranslationAdmin):
    list_display = ("full_name", "title", "position")
    list_display_links = ("full_name", "title")
    list_editable = ("position",)
    search_fields = ("full_name", "title")
    search_help_text = "Search name or title"


@admin.register(Comment)
class CommentAdmin(TranslationAdmin):
    list_display = ("user_full_name", "rate", "comment", "is_active")
    list_editable = ("is_active", "rate")
    list_display_links = ("user_full_name",)
