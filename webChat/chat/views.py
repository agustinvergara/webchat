from django.shortcuts import render
from django.http import JsonResponse
from .models import Message

def chat(request):
    messages = Message.objects.all()
    return render(request, 'chat/chat.html', {'messages': messages})

def send_message(request):
    if request.method == 'POST':
        username = request.POST['username']
        content = request.POST['content']
        # sent_time = request.POST['content']
        message = Message(username=username, content=content)
        message.save()          
        return JsonResponse({'status': 'ok'})
    else:
        return JsonResponse({'status': 'error'})
    