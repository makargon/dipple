from rest_framework import serializers

from apps.bulb.models import News, Comments

class NewsSerializer(serializers.ModelSerializer): # HyperlinkedModelSerializer
    class Meta:
        model = News
        fields = (
            'id', 
            'title', 
            'description', 
            'action_click', 
            'main_img_url', 
            'tags', 
            'publish_date', 
            'rating')