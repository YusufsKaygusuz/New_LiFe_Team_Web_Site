from life.models import NewLifeManagementMember
from modeltranslation.translator import TranslationOptions,register


@register(NewLifeManagementMember)
class NewLifeManagementMemberTranslationOptions(TranslationOptions):
    fields = ('title',)
