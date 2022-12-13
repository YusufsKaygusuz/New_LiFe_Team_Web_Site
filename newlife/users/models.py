from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, ImageField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


def user_profile_image_path(instance, filename):
    return f"users/profile-image/{instance.id}/{filename}"


class User(AbstractUser):
    """
    Default custom user model for newlife.
    If adding fields that need to be filled at user signup,
    """

    #: First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True, max_length=255)
    first_name = None  # type: ignore
    last_name = None  # type: ignore
    profile_image = ImageField(
        verbose_name=_("Profile Image"), upload_to=user_profile_image_path, blank=True
    )

    def get_absolute_url(self):
        """Get url for user's detail view.
        Returns:
            str: URL for user detail.
        """
        return reverse("users:detail", kwargs={"username": self.username})
