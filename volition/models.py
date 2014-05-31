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

# Training <-many:one- Volunteer
class Training(models.Model):
    YEAR_CHOICE = [(-1,'-1',)]
    YEAR_CHOICE.extend(map(
        lambda x: (x, str(x)),
        range(datetime.now().year, 1979, -1)))

    # A Volunteer is the foreign key for Training
    volunteer = models.ForeignKey(
        Volunteer,
        on_delete=models.CASCADE
    )

    # Training information
    name = models.CharField(
        max_length=120,
        null=False
    )
    year = models.IntegerField(
        choices=YEAR_CHOICE,
        null=False,
        default=datetime.now().year
    )
    location = models.CharField(
        max_length=254,
        blank=True,
        null=True,
        default=None
    )
    expiration_year = models.IntegerField(
        choices=YEAR_CHOICE,
        null=False,
        default=-1
    )
    remind = models.BooleanField(
        verbose_name="Remind when expiring?",
        null=False,
        default=False
    )
    #TODO: approved? status, upload credential pic, month/day expiry ?

    # Meta options
    class Meta:
        verbose_name = "training and qualifications"
        verbose_name_plural = "training and qualifications"
        ordering = ['name', '-year', '-expiration_year']

    # Human-friendly read format
    def __unicode__(self):
        return u'%s (%d), Expires: %d' %(
            self.name, self.year,
            self.expiration_year if self._expiration_year is not None else 'Never',
        )

# Experiences <-many:one- Volunteer
class Experience(models.Model):
    YEAR_CHOICE = map(
        lambda x: (x, str(x)),
        range(datetime.now().year, 1979, -1))

    # A Volunteer is the foreign key for an Experience
    volunteer = models.ForeignKey(
        Volunteer,
        on_delete=models.CASCADE
    )

    # Event/experience information
    event_year = models.IntegerField(
        choices=YEAR_CHOICE,
        null=False,
        default=datetime.now().year
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
        verbose_name_plural = "events experience"
        ordering = ['-event_year', 'event_name']

    # Human-friendly read format
    def __unicode__(self):
        return u'%s (%d) : %d h' % (
            self.event_name, self.event_year, self.work_hours
        )

