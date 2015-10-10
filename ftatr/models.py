import datetime
from django.core.mail import send_mail
from django.db import models
from ftatr import settings


class ContactMessage(models.Model):
    sender = models.CharField(max_length=100, blank=False, null=False)
    subject = models.CharField(max_length=100, blank=False, null=False)
    message = models.TextField(blank=False, null=False)

    created_at = models.DateTimeField(blank=False, null=False)

    def __str__(self):
        return "From {sender} on {created_at}".format(sender=self.sender,
                                                      created_at=self.created_at.isoformat())

    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = datetime.datetime.now()
        super().save(*args, **kwargs)

    @property
    def email_subject(self):
        return "New contact message: {subject}".format(subject=self.subject)

    @property
    def email_message(self):
        return """
New message sent through the contact form!
Message created on {created_at}


Sender: {sender}
Subject: {subject}
Message: {message}""".format(created_at=str(self.created_at),
                             subject=self.subject,
                             sender=self.sender,
                             message=self.message)

    def send(self):
        send_mail(subject=self.email_subject,
                  message=self.email_message,
                  from_email='no-reply@forthoseabouttorock.io',
                  recipient_list=[admin[1] for admin in settings.ADMINS])
