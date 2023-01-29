from django.db import models
from django.utils.translation import gettext_lazy as _


class CommentStarChoices(models.TextChoices):
    STAR_1 = "1", _("1 Star")
    STAR_2 = "2", _("2 Star")
    STAR_3 = "3", _("3 Star")
    STAR_4 = "4", _("4 Star")
    STAR_5 = "5", _("5 Star")


class ClassesChoices(models.TextChoices):
    CLASS_10 = "10sinif", _("10. Sınıf")
    CLASS_11 = "11sinif", _("11. Sınıf")
    CLASS_12 = "12sinif", _("12. Sınıf")
    UNI = "uni", _("Universite")


class ClassesTestChoices(models.TextChoices):
    CLASS_09 = "9sinif", _("9. Sınıf")
    CLASS_10 = "10sinif", _("10. Sınıf")
    CLASS_11 = "11sinif", _("11. Sınıf")
    CLASS_12 = "12sinif", _("12. Sınıf")
    UNI = "uni", _("Universite")
