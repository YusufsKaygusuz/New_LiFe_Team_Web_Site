from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, ImageField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.db import models


def user_profile_image_path(instance, filename):
    return f"users/profile-image/{instance.id}/{filename}"


class User(AbstractUser):
    """
    Default custom user model for newlife.
    If adding fields that need to be filled at user signup,
    """

    class UserClassesChoices(models.TextChoices):
        CLASS_9 = "9sinif", _("9. Sınıf")
        CLASS_10 = "10sinif", _("10. Sınıf")
        CLASS_11 = "11sinif", _("11. Sınıf")
        CLASS_12 = "12sinif", _("12. Sınıf")
        UNI = "uni", _("Universite")

    #: First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True, max_length=255)
    first_name = None  # type: ignore
    last_name = None  # type: ignore
    profile_image = ImageField(
        verbose_name=_("Profile Image"), upload_to=user_profile_image_path, blank=True
    )
    class_choices = models.CharField(choices=UserClassesChoices.choices,blank=True,max_length=7)
    university = models.CharField(verbose_name="University",blank=True,max_length=255)

    def get_absolute_url(self):
        """Get url for user's detail view.
        Returns:
            str: URL for user detail.
        """
        return reverse("users:detail", kwargs={"username": self.username})
