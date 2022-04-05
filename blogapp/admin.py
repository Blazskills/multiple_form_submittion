from django.contrib import admin

from .models import ActivityStream, ActivityStreamTarget, NewComer, Memebers


# Register your models here.

@admin.register(NewComer)
class NewComer(admin.ModelAdmin):
    #  autocomplete_fields = ['name']
    list_display = ['id', 'name', 'email', 'phone', 'home_address', 'contact_via',
                    'invited_by', 'intrest', 'prayer_request', 'observations', 'current_job']
    search_fields = ["name", "pk__id"]
    # list_filter = ['name']


@admin.register(Memebers)
class Memebers(admin.ModelAdmin):
    #  autocomplete_fields = ['name']
    list_display = ['id', 'name', 'email', 'phone',
                    'home_address', 'contact_via', 'memeber_type', 'current_job']
    search_fields = ["name", "memeber_type"]
    # list_filter = ['name', 'memeber_type']


@admin.register(ActivityStream)
class ActivityStreamAdmin(admin.ModelAdmin):
    #  autocomplete_fields = ['created_by']
    list_display = ['id', 'user', 'verb',
                    'ref_id', 'response_status',  'created']
    search_fields = ["verb", "ref_id"]
    # list_filter = ['created', 'verb']


@admin.register(ActivityStreamTarget)
class ActivityStreamTargetAdmin(admin.ModelAdmin):
    #  autocomplete_fields = ['created_by']
    list_display = ['id', 'activity_stream',
                    'target_ct', 'target_id', 'target', 'created']
    search_fields = ["target_id"]
    # list_filter = ['created', 'activity_stream__user']
