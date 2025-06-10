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


class VideoLogs(models.Model):
    request_id=models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    video_link = models.TextField(_('video_link'),null=True,default=None)
    timestamp=models.DateTimeField(_('timestamp'), null=False,blank=False,default=timezone.now)
    class Meta:
        ordering = ["-id"]
