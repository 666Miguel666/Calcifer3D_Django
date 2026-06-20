from django.db import models


class Categoria(models.Model):
    nombre = models.CharField(
        max_length=100,
        unique=True
    )

    class Meta:
        db_table = 'categoria'

    def __str__(self):
        return self.nombre


class Marca(models.Model):
    nombre = models.CharField(
        max_length=100,
        unique=True
    )

    class Meta:
        db_table = 'marca'

    def __str__(self):
        return self.nombre


class Producto(models.Model):

    nombre = models.CharField(
        max_length=150
    )

    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.PROTECT,
        related_name='productos'
    )

    marca = models.ForeignKey(
        Marca,
        on_delete=models.PROTECT,
        related_name='productos'
    )

    color = models.CharField(
        max_length=50,
        blank=True
    )

    descripcion = models.TextField(
        blank=True
    )

    cantidad = models.PositiveIntegerField(
        default=0
    )

    precio_compra = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    precio_redes = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    precio_mercadolibre = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    precio_punto_fisico = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    ubicacion = models.CharField(
        max_length=100,
        blank=True
    )

    foto = models.ImageField(
        upload_to='productos/',
        blank=True,
        null=True
    )

    fecha_registro = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        db_table = 'producto'
        ordering = ['nombre']

    def __str__(self):
        
        return self.nombre