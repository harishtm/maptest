from django import template
from django.contrib.contenttypes.models import ContentType
from apptest.models import *

register = template.Library()


@register.assignment_tag
def get_userprofile_address(user):
    #import ipdb;ipdb.set_trace()
    userprofile_obj = None
    address_obj = None
    try:
        userprofile_obj = user.userprofile_set.all()[0]
        cont_type = ContentType.objects.get_for_model(UserProfile)
        address_obj = Address.objects.get(content_type = cont_type,object_id = userprofile_obj.id)
        print "Address",address_obj
    except:
        pass
    return (userprofile_obj,address_obj)
