from django.db import models

# Create your models here.
class Post(models.Model):
    url = models.URLField()
    author = models.TextField(max_length=50)
    author_url = models.URLField()
    text = models.TextField()
    date = models.DateTimeField()
    date_url = models.URLField()
    status = models.TextField(max_length=20, null=True)

    # def publish(self):
    #     self.published_date = timezone.now()
    #     self.save()

    #def hide(self):
    #    self.status = 'hide'
    #    self.save()


    def __str__(self):
        return self.text


class Settings(models.Model):

    filters = models.TextField()
    urls = models.TextField()
    runs = models.BooleanField(default=False)
    run_last_time = models.DateTimeField()  # время последнего запуска
    run_delay = models.IntegerField(default=5) # задержка между запусками
    status = models.CharField(default="Idle", max_length=50) 






