from django.contrib import admin

# Register your models here.
from volition.models import Volunteer, Experience

class VolunteerAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'last_name',
        'first_name',
        'email',
        'phone',
        'address',
        'is_active',
    )
    fields = ('last_name','first_name','email','phone','address','is_active',)
    search_fields = (
        'id',
        'last_name',
        'first_name',
        'email',
        'phone',
        'is_active',
    )

class ExperienceAdmin(admin.ModelAdmin):
    list_display = (
        'volunteer',
        'event_name',
        'event_year',
        'work_hours',
        'volunteer_contact_info',
    )
    fields = (
        'volunteer',
        'event_name',
        'event_year',
        'work_hours',
    )
    raw_id_fields = ('volunteer',)
    search_fields = ('event_name', 'event_year',)
    list_filter = ('volunteer','event_name','event_year',)
    ordering = ('-event_year','event_name',)

    def volunteer_contact_info(self, obj):
        phone = obj.volunteer.phone
        email = obj.volunteer.email
        phone = '_' if phone is '' else phone
        email = '_' if email is '' else email
        return "Phone: %s, Email: %s" %(phone, email,)

admin.site.register(Volunteer, VolunteerAdmin)
admin.site.register(Experience, ExperienceAdmin)

