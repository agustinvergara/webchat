import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

#esta clase va a ser un consumer que se va a encargar de los mensajes que lleguen 
#y transmitirlos en tiempo real a cualquier usuario conectado al consumer

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        #le ponemos nombre al grupo de canales que se comunicaran en tiempo real (chatgroup)
        self.room_group_name = 'test'
        #llamamos el metodo async_to_sinc para acceder a los channel layers con el  que podemos 
        #crear los grupos de canales
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        #aqui usamos del channel_layer el metodo group send para que se envie al grupo especificado
        #despues => self.room_group_name a tiempo real el mensaje
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                #tambien le damos un nombre al evento que queremos que sea manejado por una funcion
                #que va a enviar el mensaje al forntend
                'type':'chat_message',
                #este evento se llama message
                'message':message
            }
        )
        

        # print('Message:', message)

    #este metodo solo va a ense;ar los mensajes que se envian a todos
    def chat_message(self, event):
        #usamos el objeto evento para buscar el evento que se llama mensaje y asi tener esa info
        message = event['message']

        self.send(text_data=json.dumps({
            'type':'chat',
            'message':message
        }))