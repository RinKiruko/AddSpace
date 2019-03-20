from django.db import models
import uuid


class Add(models.Model):
    Title = models.CharField(verbose_name='Название',null=True, max_length=50)
    Author = models.ForeignKey('Accounts.User', models.CASCADE, null=True, 
                                verbose_name='Автор', related_name='adds')
    PostingDate = models.DateField(verbose_name='Дата добавления', null=True, 
                            auto_now_add=True, editable=False)
    Content = models.TextField(verbose_name='Содержание', null=True,)

    def __str__(self):
        return self.Title + self.Author

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Add'
        verbose_name_plural = 'Adds'