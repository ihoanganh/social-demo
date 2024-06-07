from django.urls import re_path
from core import consumers


websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer.as_asgi()),
    re_path(r'ws/group-chat/(?P<room_name>[\w-]+)/$', consumers.GroupChatConsumer.as_asgi()),
]
