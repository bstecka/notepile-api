from django.contrib.auth.models import User
from .models import Image, Note
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class ImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'src']


class NoteSerializer(serializers.HyperlinkedModelSerializer):
    images = ImageSerializer(many=True, read_only=False)
    user = UserSerializer(read_only=True)

    def create(self, validated_data):
        images_data = validated_data.pop('images')
        note = Note.objects.create(**validated_data)
        for img_dict in images_data:
            if img_dict['src']:
                Image.objects.create(src=img_dict['src'], note=note)
        return note

    def update(self, instance, validated_data):
        pk = self.context['pk']
        note = Note.objects.get(pk=pk)
        note.text = validated_data.pop('text')
        note.save()
        return note

    class Meta:
        model = Note
        fields = ['id', 'text', 'src', 'images', 'user']
