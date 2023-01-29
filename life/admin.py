from django.contrib import admin
from django.utils.html import format_html
from modeltranslation.admin import TranslationAdmin
from life.models import Card, Comment, Molecule, NewLifeManagementMember, Blog, FavoriteBlog, FavoriteMolecule, \
    MoleculeTest


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


@admin.register(Molecule)
class MoleculeAdmin(TranslationAdmin):
    def iframe(self, obj: Molecule):
        return format_html(
            f'<iframe style="width: 50%;" frameborder="0" src="{obj.embed_link}"></iframe>'
        )

    list_display = ("iframe", "title", "embed_link")
    list_display_links = ("title",)
    list_editable = ("embed_link",)


@admin.register(Card)
class CardAdmin(TranslationAdmin):
    list_display = ("question_title", "question_answer")
    list_display_links = ("question_title",)


@admin.register(Blog)
class BlogAdmin(TranslationAdmin):
    list_display = ("title",)
    list_display_links = ("title",)
    readonly_fields = ("created_at","slug")


@admin.register(FavoriteBlog)
class FavoriteBlogAdmin(admin.ModelAdmin):
    pass


@admin.register(FavoriteMolecule)
class FavoriteMoleculeAdmin(admin.ModelAdmin):
    pass


@admin.register(MoleculeTest)
class MoleculeTestAdmin(admin.ModelAdmin):
    list_display = ("title","test_id")
    list_display_links = ("title",)
    readonly_fields = ("test_id",)

