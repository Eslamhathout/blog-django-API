from rest_framework import serializers
from myblog.models import Article
from django.contrib.auth.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    #Using simple views
    # articles = serializers.HyperlinkedRelatedField(many=True, view_name='article_detail', read_only=True)

    #Using viewsets
    articles = serializers.HyperlinkedRelatedField(many=True, view_name='article-detail', read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'articles']


class articleSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100, required=False)
    #Instead of using this which just importing the already populated DB
    #author = serializers.CharField(max_length=100, required=False)
    #Now I can read it from the perform_create function.
    author = serializers.ReadOnlyField(source='author.username')
    email = serializers.EmailField(required=False)
    date = serializers.DateTimeField(required=False)


    def create(self, validated_data):
        return Article.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.author = validated_data.get('author', instance.author)
        instance.email = validated_data.get('email', instance.email)
        instance.date = validated_data.get('date', instance.date)
        instance.save()
        return instance