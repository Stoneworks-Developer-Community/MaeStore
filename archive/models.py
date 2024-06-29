from django.db import models
from snowflake import Snowflake
from MaeStore.settings import MAESTOR_GENRES, MAESTOR_WORLDS

# Create your models here.
# Create a model called Book that contains the info of a readable book entry, including a category field, author etc
class Book(models.Model):
    id = models.PositiveBigIntegerField(primary_key=True, default=Snowflake().generate().id)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=16)
    text = models.JSONField()
    genre = models.CharField(max_length=100, choices=MAESTOR_GENRES)
    world = models.CharField(max_length=100, choices=MAESTOR_WORLDS)
    lore = models.TextField(null=True)

    def __str__(self):
        return self.title
