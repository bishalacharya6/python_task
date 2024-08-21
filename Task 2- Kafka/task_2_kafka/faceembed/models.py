from django.db import models

class FaceEmbed(models.Model):
    id = models.AutoField(primary_key=True)
    age = models.IntegerField()
    emotion = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    timestamp = models.DateTimeField()

    def __str__(self):
        return f"FaceEmbed {self.id}: {self.emotion} {self.gender}"