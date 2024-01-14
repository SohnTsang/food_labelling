from django.db import models


class CustomTranslation(models.Model):
    japanese_text = models.CharField(max_length=255, unique=True)
    en_translation = models.CharField(max_length=255, blank=True, null=True)
    cn_translation = models.CharField(max_length=255, blank=True, null=True)
    th_translation = models.CharField(max_length=255, blank=True, null=True)
    kr_translation = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.japanese_text
