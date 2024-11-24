from django.db import models
from snowflake import Snowflake
from Testament.settings import TESTAMENT_GENRES, TESTAMENT_WORLDS

def new_id():
    return Snowflake().generate().id
# Create your models here.
class Book(models.Model):
    id = models.PositiveBigIntegerField(primary_key=True, default=new_id)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=16)
    text = models.JSONField()
    genre = models.CharField(max_length=100, choices=TESTAMENT_GENRES)
    world = models.CharField(max_length=100, choices=TESTAMENT_WORLDS)

    def get_absolute_url(self):
        return f'/read/{self.id}'

    # pylint: disable-next=invalid-str-returned
    def __str__(self):
        return self.title
