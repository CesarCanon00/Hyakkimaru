from django.db import models
# Create your models here.

class Lugar(models.Model):
    nombre = models.CharField(max_length=50,)
    imagen = models.ImageField(upload_to="lugares", null = True)
    def save(self):
        super(Lugar,self).save()
    def __str__(self):
        return self.nombre

class Pieza(models.Model):
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return '{}'.format(self.nombre)

class Monstruo(models.Model):
    nombre = models.CharField(max_length=30,)
    imagen = models.ImageField(upload_to="monstruos", null = True)
    pieza = models.ForeignKey(
        Pieza,
        on_delete = models.CASCADE,
    )
    lugar = models.ForeignKey(
        Lugar,
        on_delete = models.CASCADE,
    )
    def save(self):
        super(Monstruo,self).save()
    class Meta:
        verbose_name_plural = 'Monstruos'
    
    def __str__(self):
        return '{}'.format(self.nombre)


class Pelea(models.Model):
    lugar = models.ForeignKey(
        Lugar,
        on_delete = models.CASCADE
    )
    monstruo = models.ForeignKey(
        Monstruo,
        on_delete = models.CASCADE
    )
    def save(self):
        super(Pelea,self).save()
    class Meta:
        verbose_name_plural = 'Peleas'
    
    def __str__(self):
        return '{}'.format(self)

class Objeto(models.Model):
    nombre = models.CharField(max_length=30,)
    ROBO = 'Robo'
    COMPRA = 'Compra'
    REGALO = 'Regalo'
    ESTADOS_CHOICES = [
        (ROBO, 'Robo'),
        (COMPRA, 'Compra'),
        (REGALO, 'Regalo'),
    ]
    origen = models.CharField(
        max_length=20,
        choices=ESTADOS_CHOICES,
        default=ROBO,
    )

    def save(self):
        super(Objeto,self).save()
    class Meta:
        verbose_name_plural = 'Objetos'
    
    def __str__(self):
        return '{}'.format(self)
