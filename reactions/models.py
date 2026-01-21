from django.db import models
from authApp.models import User

class Reaction_type(models.TextChoices):
    LIKE = 'like', 'Like'
    DISLIKE = 'dislike', 'Dislike'


class Reaction(models.Model):
    reaction = models.CharField(verbose_name='reaction', choices=Reaction_type, blank=True, null=True)
    reacted_at = models.DateTimeField(("Reacted at"), auto_now=False, auto_now_add=True)

    def __str__(self):
        return f"{self.reaction}"



