from django.db import models
# Create your models here.

class Artist(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    country = models.CharField(max_length=100)
    disambiguation = models.TextField(max_length=200)

    def __str__(self):
        return 'Artist: ' + self.name

class Label(models.Model):
    name = models.CharField(max_length=100)
    labelcode= models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return 'Label: ' + self.name

class Release(models.Model):
    title = models.CharField(max_length=150)
    date= models.DateField()
    country = models.CharField(max_length=150)
    artist = models.ForeignKey('Artist' , on_delete=models.SET_NULL , null=True)
    label = models.ForeignKey('Label', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return 'Release: ' + self.title

class ReleaseGroup(models.Model):
    firstrelease= models.DateField()
    title = models.CharField(max_length=150)
    release = models.ForeignKey('Release' , on_delete=models.SET_NULL , null=True)
    type = models.CharField(max_length=150)

class Recording(models.Model):
    title = models.CharField(max_length=150)
    disambiguation = models.CharField(max_length=150)
    artist = models.ForeignKey('Artist', on_delete=models.SET_NULL, null=True)
    release = models.ForeignKey('Release', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return 'Recording: ' + self.title

class Work(models.Model):
    title = models.CharField(max_length=150)
    language = models.CharField(max_length=150)
    recording = models.ForeignKey('Recording', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return 'Work: ' + self.title