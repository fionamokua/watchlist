from rest_framework import serializers
from ..models import WatchList,StreamingPlartform


class WatchListSerializers(serializers.ModelSerializer):
    #len_name= serializers.SerializerMethodField()
    class Meta:
        model=WatchList
        #fields=['id','name','description','active']
        fields="__all__"
        #exclude=['name']
class StreamingPlatformSerializer(serializers.ModelSerializer):
    watchlist=WatchListSerializers(many=True,read_only=True)
    # watchlist=serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name="streamdetail")
    #watchlist= serializers.StringRelatedField(many=True,read_only=True)
    class Meta:
        model=StreamingPlartform
        fields="__all__"
    
    # def get_len_name(self, object):
      
    #     return len(object.name)
    # def validate(self, data):
    #     if data['name'] == data['description']:
    #         raise serializers.ValidationError("Title cannot be description")
    #     return data
    # def validate_name(self,value):
    #     if len(value) < 2:
    #         raise serializers.ValidationError("Name is too short")
        
    #     return value
# def name_length(value):
#     if len(value) < 2:
#             raise serializers.ValidationError("Name is too short")
        
#     return value
    
# class MovieSerializers(serializers.Serializer):
#     id =serializers.IntegerField(read_only=True)
#     name=serializers.CharField( validators=[name_length])
#     description = serializers.CharField()
#     active=serializers.BooleanField()
#     def create(self, validated_data):
        
#         return Movie.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name',instance.name)
#         instance.description = validated_data.get('description',instance.description)
#         instance.active= validated_data.get('active',instance.active)
#         instance.save()
#         return instance
    
#     def validate(self, data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError("Title cannot be description")
#         return data
#     # def validate_name(self,value):
#     #     if len(value) < 2:
#     #         raise serializers.ValidationError("Name is too short")
        
#     #     return value