from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
# Create your models here.


class UserProfile(models.Model):
    user = models.ForeignKey(User)
    description = models.CharField(max_length=255,blank=True,null=True)
    phone1 = models.CharField(max_length = 20, blank = True, null = True)

    def __unicode__(self):
        return self.user.username


class Address(models.Model):
    content_type = models.ForeignKey(ContentType, verbose_name=_('content type'), related_name="content_type_set_for_%(class)s")
    object_id = models.TextField(_('object ID'))
    address1 = models.CharField(max_length = 100, blank = True, null = True)
    pincode = models.CharField(max_length = 100, blank = True, null = True)
    state = models.CharField(max_length = 100, blank = True, null = True)
    country = models.CharField(max_length = 100, blank = True, null = True)

