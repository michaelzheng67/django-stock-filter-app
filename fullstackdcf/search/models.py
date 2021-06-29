from django.db import models

# Create your models here.
class tickersymbol(models.Model):
    ticker = models.CharField(max_length=5)

    def get_absolute_url(self):
        return "tickersymbol/analysis"
