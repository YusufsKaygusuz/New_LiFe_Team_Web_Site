from django.db import models
from django.utils.translation import gettext_lazy as _


class CommentStarChoices(models.TextChoices):
    STAR_1 = "1", _("1 Star")
    STAR_2 = "2", _("2 Star")
    STAR_3 = "3", _("3 Star")
    STAR_4 = "4", _("4 Star")
    STAR_5 = "5", _("5 Star")
