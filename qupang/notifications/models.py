from django.db import models
from qupang.users import models as user_models
from qupang.images import models as image_models

class Notification(image_models.TimeStampedModel):

    # First one is for Database
    # Second one is for Admin

    TYPE_CHOICES = (
        ('like', 'Like'),
        ('comment', 'Comment'),
        ('follow', 'Follow')
    )

    creator = models.ForeignKey(user_models.User, on_delete=models.CASCADE, related_name='notification_creator')
    to = models.ForeignKey(user_models.User, on_delete=models.CASCADE, related_name='notification_to')
    notification_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    image = models.ForeignKey(image_models.Image, null=True, blank=True, on_delete=models.CASCADE)
    comment = models.CharField(null=True, blank=True, max_length=140)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return 'From:{} - To:{}'.format(self.creator, self.to)