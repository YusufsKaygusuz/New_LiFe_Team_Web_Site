from django.db import models
from django.utils.translation import gettext_lazy as _

from life.choices import CommentStarChoices


def management_member_image_path(instance, filename):
    return f"management-member/image/{instance.id}/{filename}"


def comment_user_image_path(instance, filename):
    return f"comment-user/image/{instance.id}/{filename}"


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
    linkedin = models.URLField(
        verbose_name=_("Linkedin URL"), help_text="Linkedin link", blank=True
    )
    instagram = models.URLField(
        verbose_name=_("Instagram URL"), help_text="Instagram link", blank=True
    )
    position = models.PositiveSmallIntegerField(
        verbose_name=_("Ordering Number"), unique=True
    )
    image = models.ImageField(
        verbose_name=_("Member Image"),
        upload_to=management_member_image_path,
        blank=True,
    )

    class Meta:
        verbose_name = _("Management Member")
        verbose_name_plural = _("Management Members")
        ordering = ("position",)


class Comment(models.Model):
    user_full_name = models.CharField(
        verbose_name=_("User Full Name"), help_text="ex: Berkay Şen", max_length=255
    )
    user_image = models.ImageField(
        verbose_name=_("User Image"), upload_to=comment_user_image_path, blank=True
    )
    rate = models.CharField(
        verbose_name=_("Comment Star"),
        help_text="ex: 4",
        choices=CommentStarChoices.choices,
        max_length=3,
    )
    comment = models.TextField(
        verbose_name=_("User Comment"), help_text="ex: Very nice.."
    )
    is_active = models.BooleanField(
        verbose_name=_("Is Active Comment"), help_text="Is published", default=False
    )

    def __str__(self) -> str:
        return f"{self.user_full_name.title()} - {self.comment}"

    def get_total_range(self):
        return range(0, int(self.rate))

    class Meta:
        verbose_name = _("User Comment")
        verbose_name_plural = _("User Comments")
