import random
from blogapp.models import ActivityStream, ActivityStreamTarget
from django.contrib.contenttypes.models import ContentType
from string import digits


def generate_digits(length):
    code = ""
    for i in range(length):
        code += random.choice(digits)
    return code


def create_activity_stream(user, verb, ref_id, response_status='Attempt', target=None):
    action = ActivityStream(user=user if user.is_authenticated else '',
                            verb=verb, ref_id=ref_id, response_status=response_status)
    action.save()
    if isinstance(target, list):
        for t in target:
            ActivityStreamTarget.objects.create(
                target=t, activity_stream=action
            )
        return
    ActivityStreamTarget.objects.create(
                target=target, activity_stream=action
            )


def update_activity_stream(ref_id,  verb, response_status, user='', target=None,):
    print(ref_id)
    create_activity_stream(
        user=user,
        verb=verb, ref_id=ref_id, response_status=response_status, target=target
    )




def delete_multiple_element(list_object, indices):
    indices = sorted(indices, reverse=True)
    for idx in indices:
        if idx < len(list_object):
            list_object.pop(idx)