from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
# Create your models here.

class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    # created_by = models.ForeignKey('account.User', on_delete=models.CASCADE, null=True, blank=True,
    #                                related_name='+')


CONTACTED_BY = (
    ('CALL', "CALL"),
    ('VISIT', "VISIT"),
    ('CALL_VISIT', "CALL & VISIT"),
)


PURPOSE = (
    ('INTRESTED_IN_BECOMING_A_MEMBER', "INTRESTED IN BECOMING A MEMBER"),
    ('VISING_INTRESTED_IN_BECOMING_A_MEMBER', "VISING INTRESTED IN BECOMING A MEMBER"),
    ('SEASONAL_VISITOR_BECOMING_ACTIVE', "SEASONAL VISITOR BECOMING ACTIVE"),
    ('JUST_VISITING', "JUST VISITING")
)


MEMBER_TYPE = (
    ('FULL_MEMBER', "FULL MEMBER"),
    ('ORDINARY_MEMBER', "ORDINARY_MEMBER")
)


ACTIVITY_STREAM_CHOICES = (
    ('Attempt', "Attempt"),
    ('Success', "Success"),
    ('Failed', "Failed"),
)


class NewComer(BaseModel):
    name = models.CharField(max_length=64)
    email = models.CharField(max_length=64, null=True)
    phone =  models.CharField(max_length=64)
    home_address= models.CharField(max_length=64)
    contact_via = models.CharField(max_length=200, choices=CONTACTED_BY, default="CALL")
    invited_by = models.CharField(max_length=64, null=True)
    intrest = models.CharField(max_length=200, choices=PURPOSE, default="JUST_VISITING")
    prayer_request = models.CharField(max_length=64, null=True)
    observations = models.CharField(max_length=64, null=True)
    current_job = models.CharField(max_length=64, null=True)


    def __str__(self):
        return "%s (%s)" % (self.name, self.email)
    
    class Meta:
        verbose_name = "Newcomer List"
    
    
class Memebers(BaseModel):
    name = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    phone =  models.CharField(max_length=64)
    home_address= models.CharField(max_length=64)
    contact_via = models.CharField(max_length=200, choices=CONTACTED_BY, default="CALL")
    memeber_type=models.CharField(max_length=200, choices=MEMBER_TYPE, default="ORDINARY_MEMBER")
    current_job = models.CharField(max_length=64, null=True)
    
    # class Meta:
    #     verbose_name = "Members List"


    def __str__(self):
        return "%s (%s)" % (self.name, self.email)
    
    
    class Meta:
            ordering = ('-created',)

class ActivityStream(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE,  related_name='actions', db_index=True, null=True, blank=True)
    verb = models.CharField(max_length=255)
    ref_id = models.CharField(max_length=255)
    response_status = models.CharField(max_length=20, choices=ACTIVITY_STREAM_CHOICES, default='ATTEMPT')
    
    
    def __str__(self):
        return f"{self.ref_id}"
    class Meta:
        ordering = ('-created',)

class ActivityStreamTarget(BaseModel):
    activity_stream = models.ForeignKey(ActivityStream, related_name='activitystream', on_delete=models.CASCADE)
    target_ct = models.ForeignKey(ContentType, blank=True, null=True, related_name='target_obj', on_delete=models.CASCADE)
    target_id = models.PositiveIntegerField(null=True, blank=True, db_index=True)
    target = GenericForeignKey('target_ct', 'target_id')

    def __str__(self):
        return f"{self.target_id}"