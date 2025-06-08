from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid


from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid
from django.utils import timezone
# Create your models here.

def nameFile(instance, filename):
    """
    Custom function for naming image before saving.
    """
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)

    return 'uploads/{filename}'.format(filename=filename)


class Recepient(models.Model):
    request_id=models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    fullname=models.CharField(_('fullname'),max_length=255,blank=True,null=True)
    phone_number=models.CharField(_('phone_number'),max_length=255,
                                  blank=True,null=True)
    email=models.CharField(_('email'),max_length=255,blank=True,null=True)
    class Meta:
        ordering = ["-id"]
