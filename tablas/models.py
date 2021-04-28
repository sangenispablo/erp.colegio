from django.db import models
from django.forms import model_to_dict


class Nivel(models.Model):
    detalle = models.CharField('Detalle', max_length=200)
    creado_el = models.DateTimeField(auto_now_add=True)
    actualizado_el = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.detalle

    # Este metodo sirve para pasar la instancia a un Diccionario (JSON)
    def toJSON(self):
        return model_to_dict(self)

    class Meta:
        verbose_name_plural = 'niveles'
        db_table = verbose_name_plural


class Turno(models.Model):
    detalle = models.CharField('Detalle', max_length=200)
    creado_el = models.DateTimeField(auto_now_add=True)
    actualizado_el = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.detalle

    class Meta:
        verbose_name_plural = 'turnos'
        db_table = verbose_name_plural


class Aula(models.Model):
    nivel = models.ForeignKey(Nivel, related_name='aulas', on_delete=models.CASCADE)
    turno = models.ForeignKey(Turno, related_name='aulas', on_delete=models.CASCADE)
    curso = models.CharField('Curso', max_length=4)
    division = models.CharField('División', max_length=4)
    detalle = models.CharField('Nombre Completo', max_length=200)
    creado_el = models.DateTimeField(auto_now_add=True)
    actualizado_el = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.detalle

    # Pongo en mayusculas los campos curso, division, detalle
    def save(self, *args, **kwargs):
        self.curso = self.curso.upper()
        self.division = self.division.upper()
        self.detalle = self.detalle.upper()
        super(Aula, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'aulas'
        db_table = verbose_name_plural
        unique_together = ['nivel', 'turno', 'curso', 'division']
