from django.db import models

class Lead(models.Model):
    first_name = models.CharacterField()
