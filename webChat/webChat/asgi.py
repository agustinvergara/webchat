"""
ASGI config for webChat project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "webChat.settings")
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import chat.routing


#this is going to control the protocols in the asgi server 
application = ProtocolTypeRouter({
    'http':get_asgi_application(),
    #adding websocket protocol to the asgi server
    'websocket':AuthMiddlewareStack(
        URLRouter(
            #passing the urls patterns list that we created to the url router in the asgi server
            chat.routing.websockets_urlpatterns
        )
    )
})
