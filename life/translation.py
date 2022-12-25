from modeltranslation.translator import TranslationOptions, register

from life.models import Card, Comment, Molecule, NewLifeManagementMember,Blog


@register(NewLifeManagementMember)
class NewLifeManagementMemberTranslationOptions(TranslationOptions):
    fields = ("title",)


@register(Comment)
class CommentTranslationOptions(TranslationOptions):
    fields = ("comment",)


@register(Molecule)
class MoleculeTranslationOptions(TranslationOptions):
    fields = ("title", "description")


@register(Card)
class CardTranslationOptions(TranslationOptions):
    fields = ("question_title", "question_answer")


@register(Blog)
class BlogTranslationOptions(TranslationOptions):
    fields = ("title","description")
