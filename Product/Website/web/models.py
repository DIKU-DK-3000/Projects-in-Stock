from django.db import models

#Model used for storing projects
class Project(models.Model):
    title = models.CharField(max_length = 120) #120 is up for discussion
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now = False, auto_now_add = True)
    degree_choices = (('BSc','Bachelor'),('MS','Masters'))
    degree = models.CharField(max_length = 5, choices = degree_choices, default='BSc')
    topic = models.CharField(max_length = 120) #120 is up for discussion

    def __str__(self):
        return self.title

class Counselor(models.Model):
    readonly_fields=('account_id',)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    study_area = models.CharField(max_length=255)
    office = models.CharField(max_length=255)
    projects = models.ManyToManyField(Project)
    account_id = models.IntegerField(default=-1)

    def __str__(self):
        return self.name

    def is_registered(self):
        return not self.account_id == -1