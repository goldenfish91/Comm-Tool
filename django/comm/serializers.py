from django.forms import widgets
from rest_framework import serializers
from comm.models import User, Room, Message

# Get list of online users
# Get last 100 messages

class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ('name', 'online')

class RoomSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Room
		fields = ('name', 'description', 'public')

class MessageSerializer(serializers.HyperlinkedModelSerializer):
	room = serializers.HyperlinkedRelatedField(view_name='room-detail', read_only=True)
	class Meta:
		model = Message
		fields = ('text', 'time', 'room', 'user', 'at_message')
