from django_elasticsearch_dsl import Document,fields
from django_elasticsearch_dsl.registries import registry
from blogapp.models import NewComer, ActivityStream
from django.contrib.auth.models import User


@registry.register_document
class NewcomerDocument(Document):
    class Index:
        name = 'newcomer'
    settings = {
        'number_of_shards': 1,
        'number_of_replicas': 0,
        
    }
    class Django:
         model = NewComer
         fields =  ['id', 'name', 'email', 'phone', 'home_address', 'contact_via',
                    'invited_by', 'intrest', 'prayer_request', 'observations', 'current_job','created']
 


@registry.register_document
class ActivitystreamDocument(Document):
    
    user= fields.NestedField(properties={
        'username': fields.TextField(),
        'first_name': fields.TextField(),
        'last_name': fields.TextField(),
        'email': fields.TextField(),
      }, include_in_root=True)
  
    class Index:
        name = 'activitystream'
    settings = {
        'number_of_shards': 1,
        'number_of_replicas': 0,
        
    }
    class Django:
         model = ActivityStream
         fields =  ['id', 'verb',
                    'ref_id', 'response_status', 'created']
         
        #  related_models = [User]
         related_models = [User]
    
    def get_instances_from_related(self, related_instance):
            """If related_models is set, define how to retrieve the Book instance(s) from the related model."""
            if isinstance(related_instance, ActivityStream):
                return related_instance.user_set.all()


        

         
# @registry.register_document
# class ActivitystreamDocument(Document):
    
#     user= fields.ObjectField(properties={"username": fields.TextField()})
#     # fname= fields.ObjectField(properties={"first_name": fields.TextField()})
    
    
#     class Index:
#         name = 'activitystream'
#     settings = {
#         'number_of_shards': 1,
#         'number_of_replicas': 0,
        
#     }
#     class Django:
#          model = ActivityStream
#          fields =  ['id', 'verb',
#                     'ref_id', 'response_status', 'created']
         
#         #  related_models = [User]
#          related_models = ['actions']
         