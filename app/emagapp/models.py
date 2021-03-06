from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from .managers import CustomUserManager
from django.db import models
import datetime


class User(AbstractBaseUser, PermissionsMixin):
    email                       =   models.EmailField(_('email address'), unique=True)
    full_name                   =   models.CharField(max_length=255, null=True, blank=True)
    dept_name                   =   models.CharField(max_length=255, null=True, blank=True)
    phone_no                    =   models.CharField(max_length=10, null=True, blank=True)
    is_staff                    =   models.BooleanField(default=False)
    is_active                   =   models.BooleanField(default=True)
    date_joined                 =   models.DateTimeField(default=timezone.now)

    USERNAME_FIELD              =   'email'
    REQUIRED_FIELDS             =   ['full_name', 'dept_name', ]

    objects                     =   CustomUserManager()


    class Meta:
        db_table                =   'Administrators'
        verbose_name            =   'Administrator'
        verbose_name_plural     =   'Administrators'


    def __str__(self):
        return str(self.full_name)

class Subscriber(models.Model):
    email_address               =   models.EmailField(_('email address'), unique=True)


    class Meta:
        db_table                =   'Subscribers'
        verbose_name            =   'Subscriber'
        verbose_name_plural     =   'Subscribers'    


    def __str__(self):
        return str(self.email_address)


class Project(models.Model):
    user_id                     =   models.ForeignKey(to=User, on_delete=models.CASCADE, null=True, related_name='projects')
    project_title               =   models.CharField(max_length=755, null=False, blank=False, unique=True)
    project_description         =   models.TextField(null=False, blank=False)
    project_tags                =   models.CharField(max_length=400, null=True, blank=True)
    project_data                =   models.FileField(null=True, blank=True)
    project_banner              =   models.ImageField(null=True, blank=True)
    uploaded_at                 =   models.DateField(_("Date"), default=datetime.date.today)


    class Meta:
        db_table                =   'Projects'
        verbose_name            =   'Project'
        verbose_name_plural     =   'Projects'    


    def __str__(self):
        return str(self.project_title)


class Achievement(models.Model):
    user_id                     =   models.ForeignKey(to=User, on_delete=models.CASCADE, null=True, related_name='achievements')
    achievement_title           =   models.CharField(max_length=755, null=False, blank=False, unique=True)
    achievement_field           =   models.CharField(null=False, blank=False, max_length=400)
    achievement_data            =   models.FileField(null=True, blank=True)
    achievement_banner          =   models.ImageField(null=True, blank=True)
    achievement_tags            =   models.CharField(max_length=400, null=True, blank=True)
    achievement_description     =   models.TextField(null=False, blank=False)
    uploaded_at                 =   models.DateField(default=datetime.date.today)


    class Meta:
        db_table                =   'Achievements'
        verbose_name            =   'Achievement'
        verbose_name_plural     =   'Achievements'    


    def __str__(self):
        return str(self.achievement_title)


EVENT_CHOICES = (
    ("Fest", "Fest"),
    ("Workshop", "Workshop"),
    ("Activity", "Activity")
)


class Event(models.Model):
    user_id                     =   models.ForeignKey(to=User, on_delete=models.CASCADE, null=True, related_name='events', blank=True)
    event_title                 =   models.CharField(max_length=755, null=False, blank=False, unique=True)
    event_category              =   models.CharField(null=False, blank=False, max_length=400, choices=EVENT_CHOICES)
    event_tags                  =   models.CharField(max_length=400, null=True, blank=True)
    organised_by                =   models.CharField(max_length=1000, null=True, blank=True)
    sponsored_by                =   models.CharField(max_length=1000, null=True, blank=True)
    event_data                  =   models.FileField(null=True, blank=True)
    event_banner                =   models.ImageField(null=True, blank=True)
    event_description           =   models.TextField(null=False, blank=False)
    event_date                  =   models.DateField(null=False, blank=False)
    uploaded_at                 =   models.DateField(default=datetime.date.today)


    class Meta:
        db_table                =   'Events'
        verbose_name            =   'Event'
        verbose_name_plural     =   'Events'    


    def __str__(self):
        return str(self.event_title)