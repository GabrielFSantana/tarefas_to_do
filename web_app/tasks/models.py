from django.db import models

class Task(models.Model):
    STATUS_CHOICES = [
        ('Pendente', 'Pendente'),
        ('Concluído', 'Concluído'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    priority = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    due_date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pendente')

    def __str__(self):
        return self.title
