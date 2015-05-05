from django.db import models


class Contribution(models.Model):
    STATUS_NEW = 'new'
    STATUS_REJECTED = 'rejected'
    STATUS_ACCEPTED = 'accepted'
    STATUSES = (
        (STATUS_NEW, 'New'),
        (STATUS_REJECTED, 'Rejected'),
        (STATUS_ACCEPTED, 'Accepted')
    )

    TYPE_ROCKING_CHAIR = 'rocking_chair'
    TYPE_DESIGNER = 'designer'
    TYPE_MANUFACTURER = 'manufacturer'
    TYPES = (
        (TYPE_ROCKING_CHAIR, 'Rocking chair'),
        (TYPE_DESIGNER, 'Designer'),
        (TYPE_MANUFACTURER, 'Manufacturer')
    )

    target_type = models.CharField(max_length=255, choices=TYPES)
    target_slug = models.CharField(max_length=255)
    attribute = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)
    content = models.TextField()
    status = models.CharField(max_length=255, choices=STATUSES, default=STATUS_NEW)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{attribute} for {target_type} {target_slug}: "{content}"'. \
            format(attribute=self.attribute,
                   target_type=self.target_type,
                   target_slug=self.target_slug,
                   content=self.content)


class Source(models.Model):
    url = models.CharField(max_length=255)
    proposal = models.ForeignKey(Contribution, related_name='sources')
