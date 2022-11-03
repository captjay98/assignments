from django.db import models

# Create your models here.

'''
simple song CRUD application. In our models.py file inside the “musicapp” application we created, you are expected to add the following Models and Attributes.

Model: Artiste, Song, Lyric
Attributes for “Artiste” : first_name, last_name, age
Attributes for “Song” : title, date released, likes, artiste_id
Attributes for “Lyric”: content, song_id'''

class Artiste(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()

    def __str__(self):
        return self.first_name + " " + self.last_name

class Song(models.Model):
    title = models.CharField(max_length=100)
    date_released = models.DateField()
    likes = models.IntegerField()
    artiste_id = models.ForeignKey(Artiste, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Lyric(models.Model):
    content = models.TextField()
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE)

    def __str__(self):
        return self.content


