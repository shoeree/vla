from django.db import models
from datetime import datetime

# Create your models here.

# Volunteers hold information about people
class Volunteer(models.Model):
    """
    Volunteer: contains information about people.
    Holds last name, first name, email address, address, phone no, etc.
    """
    # Id
    id = models.AutoField(
        primary_key=True,
        null=False,
        unique=True
    )

    # Vital info
    last_name = models.CharField(
        max_length=30,
        null=False,
        verbose_name="Last Name"
    )
    first_name = models.CharField(
        max_length=30,
        null=False,
        verbose_name="First Name"
    )
    is_active = models.BooleanField(
        default=False,
        null=False,
        verbose_name="Active Member?"
    )

    # Contact info
    email = models.EmailField(
        max_length=254,
        null=True,
        blank=True,
        default=None,
        verbose_name='e-mail:'
    )
    phone = models.CharField(
        max_length=16,
        null=True,
        blank=True,
        default=None
    )
    address = models.CharField(
        max_length=254,
        null=True,
        blank=True,
        default=None
    )
    other = models.CharField(
        max_length=120,
        null=True,
        blank=True,
        default=None
    )

    # Meta options
    class Meta:
        verbose_name = "volunteer information"
        verbose_name_plural = "volunteer information"
        ordering = ['last_name', 'first_name']

    # Human-friendly reading method
    def __unicode__(self):
        return u'%s, %s' % (
            self.last_name, self.first_name,
        )

# Experiences <-many:one- Volunteer
class Experience(models.Model):
    YEAR_CHOICE = map(
        lambda x: (x, str(x)),
        range(1980, datetime.now().year+1))

    # A Volunteer is the foreign key for an Experience
    volunteer = models.ForeignKey(
        Volunteer,
        on_delete=models.CASCADE
    )

    # Event/experience information
    event_year = models.IntegerField(
        choices=YEAR_CHOICE,
        null=False,
        default=datetime.now().year,
    )
    event_name = models.CharField(
        max_length=120,
        null=False
    )
    work_hours = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=True,
        default=4.00
    )

    # Meta options
    class Meta:
        verbose_name = "event experience"
        verbose_name_plural = "events"
        ordering = ['-event_year', 'event_name']

    # Human-friendly read format
    def __unicode__(self):
        return u'%s (%d) : %d h' % (
            self.event_name, self.event_year, self.work_hours
        )
