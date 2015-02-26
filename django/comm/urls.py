from django.conf.urls import url, include
from comm import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'rooms', views.RoomViewSet)
router.register(r'messages', views.MessageViewSet)

urlpatterns = [
	url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
