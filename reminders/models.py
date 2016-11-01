from django.db import models

# Create your models here.
from django.core.urlresolvers import reverse
from timezone_field import TimeZoneField

class Appointment(models.Model):
    name = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=15)
    time = models.DateTimeField()
    time_zone = TimeZoneField(default='US/Easten')
    
    task_id = models.CharField(max_length=50, blank=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return 'Appointment #{0} - {1}'.format(self.pk, self.name)

    def get_absolute_url(self):
        return reverse('view_appoinment', args=[self.id])