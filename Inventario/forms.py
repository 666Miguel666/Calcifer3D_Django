from django import forms
from .models import Producto


class ProductoForm(forms.ModelForm):

    class Meta:
        model = Producto

        fields = [
            'nombre',
            'categoria',
            'marca',
            'color',
            'descripcion',
            'cantidad',
            'precio_compra',
            'precio_redes',
            'precio_mercadolibre',
            'precio_punto_fisico',
            'ubicacion',
            'foto'
        ]

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),

            'categoria': forms.Select(attrs={'class': 'form-select'}),

            'marca': forms.Select(attrs={'class': 'form-select'}),

            'color': forms.TextInput(attrs={'class': 'form-control'}),

            'descripcion': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 3
                }
            ),

            'cantidad': forms.NumberInput(
                attrs={'class': 'form-control'}
            ),

            'precio_compra': forms.NumberInput(
                attrs={'class': 'form-control'}
            ),

            'precio_redes': forms.NumberInput(
                attrs={'class': 'form-control'}
            ),

            'precio_mercadolibre': forms.NumberInput(
                attrs={'class': 'form-control'}
            ),

            'precio_punto_fisico': forms.NumberInput(
                attrs={'class': 'form-control'}
            ),

            'ubicacion': forms.TextInput(
                attrs={'class': 'form-control'}
            ),

            'foto': forms.ClearableFileInput(
                attrs={'class': 'form-control'}
            ),
        }

        labels = {
            'nombre': 'Nombre del producto',
            'categoria': 'Categoría',
            'marca': 'Marca',
            'color': 'Color',
            'descripcion': 'Descripción',
            'cantidad': 'Cantidad en inventario',
            'precio_compra': 'Precio de compra',
            'precio_redes': 'Precio redes sociales',
            'precio_mercadolibre': 'Precio Mercado Libre',
            'precio_punto_fisico': 'Precio punto físico',
            'ubicacion': 'Ubicación',
            'foto': 'Fotografía'
        }

    def clean(self):
        cleaned = super().clean()

        precio_compra = cleaned.get('precio_compra')
        precio_redes = cleaned.get('precio_redes')
        precio_mercadolibre = cleaned.get('precio_mercadolibre')
        precio_punto_fisico = cleaned.get('precio_punto_fisico')

        if precio_compra and precio_redes:
            if precio_redes < precio_compra:
                raise forms.ValidationError(
                    'El precio en redes no puede ser menor al precio de compra.'
                )

        if precio_compra and precio_mercadolibre:
            if precio_mercadolibre < precio_compra:
                raise forms.ValidationError(
                    'El precio de Mercado Libre no puede ser menor al precio de compra.'
                )

        if precio_compra and precio_punto_fisico:
            if precio_punto_fisico < precio_compra:
                raise forms.ValidationError(
                    'El precio de punto físico no puede ser menor al precio de compra.'
                )

        return cleaned