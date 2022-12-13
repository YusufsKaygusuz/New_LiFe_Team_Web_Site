from modeltranslation.translator import TranslationOptions, register

from life.models import Comment, Molecule, NewLifeManagementMember


@register(NewLifeManagementMember)
class NewLifeManagementMemberTranslationOptions(TranslationOptions):
    fields = ("title",)


@register(Comment)
class CommentTranslationOptions(TranslationOptions):
    fields = ("comment",)


@register(Molecule)
class MoleculeTranslationOptions(TranslationOptions):
    fields = ("title",)
