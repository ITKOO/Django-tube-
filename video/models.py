from django.db import models

class Video(models.Model):
    #video 제목 저장
    title = models.CharField(max_length=200)
    #video key 저장
    video_key = models.CharField(max_length=12)
