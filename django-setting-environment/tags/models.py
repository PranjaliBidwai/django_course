from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class Tag(models.Model):
    """Model representing a tag."""
    label = models.CharField(max_length=255)

class TaggedItem(models.Model):
    """Model representing a tagged item."""
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    # we want to be able to tag any object, so we use a generic foreign key
    # we need to store the content type and the object id of the tagged object
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField() # every table has a primary key that is a positive integer, so we use PositiveIntegerField
    content_object = GenericForeignKey('content_type', 'object_id')
