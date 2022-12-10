from django.db import models
from django.utils.translation import gettext_lazy as _


def management_member_image_path(instance, filename):
    return "management-member/image/{0}/{1}".format(instance.id, filename)


class NewLifeManagementMember(models.Model):
    title = models.CharField(
        verbose_name=_("Title"),
        max_length=255,
        help_text="Title ( ex: Software Engineer )",
    )
    full_name = models.CharField(
        verbose_name=_("Full Name"),
        max_length=255,
        help_text="Full Name ( ex: Elon Musk )",
    )
    linkedin = models.URLField(verbose_name=_("Linkedin URL"), help_text="Linkedin link",blank=True)
    instagram = models.URLField(verbose_name=_("Instagram URL"), help_text="Instagram link",blank=True)
    position = models.PositiveSmallIntegerField(verbose_name=_("Ordering Number"), unique=True)
    image = models.ImageField(verbose_name=_("Member Image"), upload_to=management_member_image_path,blank=True)

    class Meta:
        verbose_name = _("Management Members")
        verbose_name_plural = _("Management Member")
        ordering = ("position",)
