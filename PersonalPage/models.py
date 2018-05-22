from django.db import models

from MusicShop.models import Artist, Recording

class User_Recording_Sell(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.SET_NULL, null=True)
    recording = models.ForeignKey(Recording, on_delete=models.SET_NULL, null=True)
    description = models.TextField(max_length=200)
    price = models.DecimalField(decimal_places=2, max_digits=15, blank=False)
    user = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return 'User: ' + self.user.username + ', Sell_Recording: ' + self.recording.title
