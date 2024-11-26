from django.db import models

class Request(models.Model):
    name = models.CharField(max_length=20,verbose_name="Name")
    email = models.EmailField(verbose_name="Email")
    message = models.TextField(verbose_name="Message")
    submitted_at = models.DateTimeField(auto_now_add=True, verbose_name="Submitted at")

    def __str__(self):
        return f'{self.name}({self.email}): {self.message}'


