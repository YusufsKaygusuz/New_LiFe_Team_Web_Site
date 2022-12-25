from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from multiselectfield import MultiSelectField
from life.choices import ClassesChoices, CommentStarChoices
from ckeditor.fields import RichTextField


def management_member_image_path(instance, filename):
    return f"management-member/image/{instance.id}/{filename}"

def molecule_image_path(instance, filename):
    return f"molecules/image/{instance.id}/{filename}"

def comment_user_image_path(instance, filename):
    return f"comment-user/image/{instance.id}/{filename}"

def blog_image_path(instance, filename):
    return f"blogs/image/{instance.id}/{filename}"

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


class Molecule(models.Model):
    title = models.CharField(
        verbose_name="Molecule Title", help_text="Molecule name", max_length=255
    )
    embed_link = models.URLField(
        verbose_name="Embed Link",
        help_text="ex: https://embed.molview.org/v1/?mode=balls&cid=1049",
    )
    classes = MultiSelectField(
        verbose_name="Classes", choices=ClassesChoices.choices, blank=True
    )
    description = models.TextField(verbose_name="Description", blank=True)
    image = models.ImageField(verbose_name="Image",blank=True,null=True,help_text="Molecule Image",upload_to=molecule_image_path)
    slug = models.SlugField(verbose_name="Slug",blank=True,null=True,editable=False,unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Molecule, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.title}"

    def get_all_classes(self):
        return " ".join(list(self.classes))

    class Meta:
        verbose_name = _("Molecule")
        verbose_name_plural = _("Molecules")


class Card(models.Model):
    question_title = models.CharField(
        verbose_name="Question Title", help_text="What is the ENIAC?", max_length=255
    )
    question_answer = models.CharField(
        verbose_name="Question Answer", help_text="First Computer", max_length=255
    )

    def __str__(self):
        return self.question_title

    class Meta:
        verbose_name = _("Card")
        verbose_name_plural = _("Cards")


class Blog(models.Model):
    title = models.CharField(
        verbose_name="Blog Title", help_text="Blog Title", max_length=255
    )
    short_description = models.CharField(verbose_name="Short Description",max_length=255,help_text="Gezegenler Hakkında Kısa Bir Deneyim Turu",blank=True,null=True  )
    slug = models.SlugField(verbose_name="Slug",editable=False,unique=True)
    description = RichTextField()
    image = models.ImageField(verbose_name="Image",help_text="Blog Image",upload_to=blog_image_path)
    created_at = models.DateTimeField(auto_now_add=True,blank=True,null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Blog, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _("Blog")
        verbose_name_plural = _("Blogs")
