import secrets

from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from multiselectfield import MultiSelectField
from life.choices import ClassesChoices, CommentStarChoices, ClassesTestChoices
from ckeditor.fields import RichTextField

from newlife.users.models import User


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


class FavoriteBlog(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    blog = models.ForeignKey("Blog",on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.blog.title}"


class FavoriteMolecule(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    molecule = models.ForeignKey("Molecule",on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.molecule.title}"

def gen_random_string():
    return secrets.token_hex(16)


class MoleculeTest(models.Model):
    title = models.CharField(max_length=255,verbose_name="Title")
    image = models.ImageField(upload_to="tests/images/")
    description = models.TextField()
    classes = MultiSelectField(
        verbose_name="Classes", choices=ClassesTestChoices.choices, blank=True
    )
    question_count = models.PositiveSmallIntegerField(default=1)
    test_id = models.CharField(max_length=32, unique=True, default=gen_random_string,editable=False)
    custom_js = models.TextField(blank=True,null=True)

    def get_all_classes(self):
        return " ".join(list(self.classes))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Test"
        verbose_name_plural = "Tests"


class Video(models.Model):
    video = models.FileField(verbose_name="Video",upload_to="video/")

    class Meta:
        verbose_name = "Video"
        verbose_name_plural = "Videolar"


class CodingGallery(models.Model):
    image = models.ImageField(verbose_name="Image",upload_to="coding-gallery")

    class Meta:
        verbose_name = "Kodlama Galerisi"
        verbose_name_plural = "Kodlama Galerisi"
