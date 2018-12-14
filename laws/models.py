from django.db import models

##############################################################################################
#DECLARANDO O MODEL DAS LEIS
##############################################################################################

class LawFile(models.Model):

    STATUS_CHOICES = (
                        ('Decreto','Decreto'),
                        ('Lei Complementar','Lei Complementar'),
                        ('Lei Orgânica','Lei Orgânica'),
                        ('Lei Ordinária','Lei Ordinária'),
                    )
    type_law = models.CharField(max_length=16, choices=STATUS_CHOICES,default='Decreto')
    id_law = models.AutoField(primary_key=True)
    number_law = models.PositiveIntegerField('Número', null=False)
    date_publish = models.DateField('Data da Publicação', null=False)
    name_law = models.CharField('Nome/Descrição', max_length=300, null=False)
    desc_law = models.TextField('Transcrição', null=False)
    file_law = models.FileField('Arquivo', upload_to='leis/static/files/', null=False)

    class Meta:
        verbose_name_plural = 'Leis'
        ordering = ('date_publish',)

    def __str__(self):

        return '{} - {} - {}'.format(self.type_law, self.number_law, self.name_law)
