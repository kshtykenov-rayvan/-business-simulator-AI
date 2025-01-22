from django.shortcuts import render, get_object_or_404, redirect
from .models import Store, Chat, Message

def store_list(request):
    stores = Store.objects.all()  # Получение всех магазинов
    return render(request, 'store/store_list.html', {'stores': stores})


def chat_with_store(request, store_id):
    store = get_object_or_404(Store, id=store_id)
    chat, created = Chat.objects.get_or_create(store=store, user_name="Anonymous")  # Создать чат, если его нет
    messages = Message.objects.filter(chat=chat)
    return render(request, 'store/chat.html', {'store': store, 'chat': chat, 'messages': messages})


def send_message(request):
    if request.method == 'POST':
        chat_id = request.POST.get('chat_id')
        content = request.POST.get('content')
        sender = request.POST.get('sender')  # user или consultant

        chat = get_object_or_404(Chat, id=chat_id)
        Message.objects.create(chat=chat, sender=sender, content=content)

        # Обновить страницу чата
        return redirect('chat_with_store', store_id=chat.store.id)
