from django.conf import settings
from django.db import models
from datetime import datetime
from django.utils import timezone



class Vkcity(models.Model):
    city_id = models.BigIntegerField(primary_key=True, null=False, unique=True)
    name = models.CharField(max_length = 50, unique=True)
    def __str__(self):
        return self.name


class Vkuser(models.Model):
    user_id = models.BigIntegerField()
    # name = models.CharField(default='', max_length = 50, ) #???
    city = models.ForeignKey(Vkcity) 
    url = models.URLField(default='')
    last_name = models.CharField(default='', max_length = 50, )
    first_name = models.CharField(default='', max_length = 50, )
    screen_name = models.CharField(default='',max_length = 50, )
    def __str__(self):
        return self.last_name + " " + self.first_name


class Vkpost(models.Model):
    post_id = models.BigIntegerField()
    post_url = models.URLField()
    wall_url = models.URLField()
    author = models.ForeignKey(Vkuser)
    # text = models.TextField(db_index=True)
    text = models.TextField()
    date = models.DateTimeField()
    
    # посты которые надо скрывать для пользователя
    user_ignore_post = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)
    def __str__(self):
        return self.text


class Setting(models.Model):
    run_log = models.TextField()
    # runs = models.BooleanField(default=False)
    # status = models.CharField(default="Idle", max_length=50) 


class Group_found(models.Model):
    # Группа для ключевых слов, по которым произваолить поиск в vk.com
    name = models.CharField(default="default",max_length=50)
    key_for_found = models.TextField(blank=True)
    
    def __str__(self):
        return self.name


class Url(models.Model):
    # Url`s по которым производить поиск, генерируется по ключевым словам с Group_found
    url = models.CharField(max_length=110,unique=True)
    prioritet = models.CharField(default=50,max_length=10)

    #creationDate = timezone.now()
    # time_last_check = models.DateTimeField(default=timezone.now(),blank=True)
    time_last_check = models.DateTimeField(blank=True)
    STATUS_CHOICES = (
        ("wait", "Wait"), 
        ("active", "Active"),
        ("stop", "Stop"),
    )
    status = models.CharField(max_length=15,
                              choices=STATUS_CHOICES,
                              default="Wait",
                              )

    groups = models.ManyToManyField(Group_found, blank=True)

    def __str__(self):
        return self.url


class Filter(models.Model):
    # Персональный фильтр пользователя
    name = models.CharField(max_length = 50)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    ignore_word = models.TextField(blank=True)     # исключающие слова для поиска
    mandatory_word = models.TextField(blank=True)  # обязательные слова для поиска

    author_ignore = models.ManyToManyField(Vkuser, blank=True)

    def __str__(self):
        return self.name



# class Ignor_user(models.Model):
#     user = models.ForeignKey(
#         settings.AUTH_USER_MODEL,
#         on_delete=models.CASCADE,
#     )
    # group_found = models.ForeignKey(Group_found)
    # vk_user = models.ForeignKey(Vkuser)



