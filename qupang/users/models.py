from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, URLField, TextField, ManyToManyField, ImageField
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):

    """ User Model """

    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('not-specified', 'Not specified')
    )
    # First Name and Last Name do not cover name patterns
    # around the globe.
    profile_image = ImageField(_("Profile Image"), null=True)
    name = CharField(_("Name of User"), blank=True, max_length=255)
    website = URLField(_("Website"), max_length=200, null=True)
    bio = TextField(_("Bio"), null=True)
    phone = CharField(_("Phone Number"), max_length=140, null=True)
    gender = CharField(_("Gender"), max_length=80, choices=GENDER_CHOICES, null=True)
    followers = ManyToManyField("self", verbose_name=_("followers"))
    following = ManyToManyField("self", verbose_name=_("following"))


    # def get_absolute_url(self):
    #     return reverse("users:detail", kwargs={"username": self.username})

    def __str__(self):
        return self.username
    
    @property
    def post_count(self):
        return self.images.all().count()

    @property
    def followers_count(self):
        return self.followers.all().count()

    @property
    def following_count(self):
        return self.following.all().count()