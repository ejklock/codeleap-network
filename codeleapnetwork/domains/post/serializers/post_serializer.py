from rest_framework import serializers

from ..models import Post


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields= ['id','username','title','content','created_date_time']
        

   
        