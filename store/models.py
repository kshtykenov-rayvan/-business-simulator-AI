from django.db import models

class Store(models.Model):
    name = models.CharField(max_length=100)  # Название магазина
    description = models.TextField()  # Описание магазина
    category = models.CharField(max_length=50)  # Категория (например, одежда)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Chat(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)  # Связь с магазином
    user_name = models.CharField(max_length=50)  # Имя пользователя
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Chat with {self.store.name} by {self.user_name}"


class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)  # Связь с чатом
    sender = models.CharField(max_length=50)  # Отправитель: user или consultant
    content = models.TextField()  # Текст сообщения
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message by {self.sender} at {self.timestamp}"
