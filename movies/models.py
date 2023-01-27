from django.db.models import *

# Create your models here.
class Tur(Model):
    isim = CharField(max_length=50)

    def __str__(self):
        return self.isim

class Tek(Model):
    puan = IntegerField()

    def __str__(self):
        return str(self.puan)
class Movie(Model):
    isim = CharField(max_length = 100, verbose_name="Film Adı:")
    resim = FileField(upload_to='movies/', null= True, blank= True, verbose_name="Film Afişi")
    tur = ManyToManyField('Tur', verbose_name='Film Türü')
    tek = OneToOneField('Tek', null= True, verbose_name='IMDB Puanı', on_delete=CASCADE)
    def __str__(self):
        return self.isim