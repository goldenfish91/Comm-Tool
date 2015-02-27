from comm.models import User, Room, Message # Import models from comm app
from comm.serializers import UserSerializer, RoomSerializer, MessageSerializer
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers

@api_view(('GET',))
def api_root(request, format=None):
	return Response({
		'users': reverse('user-list', request=request, format=format),
		'rooms': reverse('rooms-list', request=request, format=format),
		'messages': reverse('messages-list', request=request, format=format)
	})

# Return the main chat room
def index(request):
    return render(request, 'comm/index.html')

class UserViewSet(viewsets.ReadOnlyModelViewSet):
	#List and Detail Actions
	queryset = User.objects.all()
	serializer_class = UserSerializer

class RoomViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = Room.objects.all()
	serializer_class = RoomSerializer

class MessageViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = Message.objects.all().order_by('-time')
	serializer_class = MessageSerializer
