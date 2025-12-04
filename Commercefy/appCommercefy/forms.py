"""
Formularios de la aplicación
"""
from django import forms
from .models import Coupon, Product, SiteConfiguration
from django.utils import timezone
import random
import string

class SiteConfigurationForm(forms.ModelForm):
    """Formulario para configuración del sitio"""
    class Meta:
        model = SiteConfiguration
        fields = [
            'site_name', 'support_email', 'support_phone', 'logo',
            # Apariencia
            'bg_body', 'bg_surface', 'bg_soft', 'product_card_bg',
            'primary_color', 'primary_color_dark', 'primary_color_light',
            'secondary_color', 'secondary_color_dark',
            'accent_color', 'accent_color_dark',
            'danger_color', 'danger_color_dark', 'warning_color', 'info_color', 'success_color',
            'text_main', 'text_muted', 'text_light',
            # Legacy
            'button_hover_color', 'text_color', 'background_color',
            # Redes
            'facebook_url', 'instagram_url', 'twitter_url',
            'meta_description',
            'show_announcement', 'announcement_text'
        ]
        widgets = {
            'site_name': forms.TextInput(attrs={'class': 'form-control'}),
            'support_email': forms.EmailInput(attrs={'class': 'form-control'}),
            'support_phone': forms.TextInput(attrs={'class': 'form-control'}),
            'logo': forms.FileInput(attrs={'class': 'form-control'}),
            
            # Colors
            'bg_body': forms.TextInput(attrs={'class': 'form-control', 'type': 'color'}),
            'bg_surface': forms.TextInput(attrs={'class': 'form-control', 'type': 'color'}),
            'bg_soft': forms.TextInput(attrs={'class': 'form-control', 'type': 'color'}),
            'product_card_bg': forms.TextInput(attrs={'class': 'form-control', 'type': 'color'}),
            
            'primary_color': forms.TextInput(attrs={'class': 'form-control', 'type': 'color'}),
            'primary_color_dark': forms.TextInput(attrs={'class': 'form-control', 'type': 'color'}),
            'primary_color_light': forms.TextInput(attrs={'class': 'form-control', 'type': 'color'}),
            
            'secondary_color': forms.TextInput(attrs={'class': 'form-control', 'type': 'color'}),
            'secondary_color_dark': forms.TextInput(attrs={'class': 'form-control', 'type': 'color'}),
            
            'accent_color': forms.TextInput(attrs={'class': 'form-control', 'type': 'color'}),
            'accent_color_dark': forms.TextInput(attrs={'class': 'form-control', 'type': 'color'}),
            
            'danger_color': forms.TextInput(attrs={'class': 'form-control', 'type': 'color'}),
            'danger_color_dark': forms.TextInput(attrs={'class': 'form-control', 'type': 'color'}),
            'warning_color': forms.TextInput(attrs={'class': 'form-control', 'type': 'color'}),
            'info_color': forms.TextInput(attrs={'class': 'form-control', 'type': 'color'}),
            'success_color': forms.TextInput(attrs={'class': 'form-control', 'type': 'color'}),
            
            'text_main': forms.TextInput(attrs={'class': 'form-control', 'type': 'color'}),
            'text_muted': forms.TextInput(attrs={'class': 'form-control', 'type': 'color'}),
            'text_light': forms.TextInput(attrs={'class': 'form-control', 'type': 'color'}),
            
            'button_hover_color': forms.TextInput(attrs={'class': 'form-control', 'type': 'color'}),
            'text_color': forms.TextInput(attrs={'class': 'form-control', 'type': 'color'}),
            'background_color': forms.TextInput(attrs={'class': 'form-control', 'type': 'color'}),
            
            'facebook_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://facebook.com/...'}),
            'instagram_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://instagram.com/...'}),
            'twitter_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://twitter.com/...'}),
            'meta_description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'show_announcement': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'announcement_text': forms.TextInput(attrs={'class': 'form-control'}),
        }

class CouponForm(forms.ModelForm):
    """Formulario para crear/editar cupones"""
    class Meta:
        model = Coupon
        fields = ['code', 'discount_percentage', 'valid_from', 'valid_to', 'active', 'usage_limit']
        widgets = {
            'valid_from': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'valid_to': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'code': forms.TextInput(attrs={'class': 'form-control'}),
            'discount_percentage': forms.NumberInput(attrs={'class': 'form-control'}),
            'usage_limit': forms.NumberInput(attrs={'class': 'form-control'}),
            'active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class BulkDiscountForm(forms.Form):
    """Formulario para aplicar o quitar descuentos masivos a productos"""
    name = forms.CharField(
        max_length=100, 
        label="Nombre de la Oferta", 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Oferta Verano 2025'})
    )
    products = forms.ModelMultipleChoiceField(
        queryset=Product.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label="Seleccionar Productos"
    )
    discount_percentage = forms.IntegerField(
        min_value=0, 
        max_value=100, 
        label="Porcentaje de Descuento",
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    action = forms.ChoiceField(
        choices=[('apply', 'Aplicar Descuento'), ('remove', 'Quitar Descuento')],
        widget=forms.Select(attrs={'class': 'form-select'}),
        label="Acción"
    )

class CouponGenerationForm(forms.Form):
    """Formulario para generar múltiples cupones en lote"""
    quantity = forms.IntegerField(min_value=1, max_value=100, label="Cantidad de Cupones", widget=forms.NumberInput(attrs={'class': 'form-control'}))
    discount_percentage = forms.IntegerField(min_value=1, max_value=100, label="Porcentaje de Descuento", widget=forms.NumberInput(attrs={'class': 'form-control'}))
    valid_days = forms.IntegerField(min_value=1, label="Días de Validez", widget=forms.NumberInput(attrs={'class': 'form-control'}))
    usage_limit = forms.IntegerField(min_value=0, initial=1, label="Límite de Uso (0 = ilimitado)", widget=forms.NumberInput(attrs={'class': 'form-control'}))
    prefix = forms.CharField(max_length=10, required=False, label="Prefijo (Opcional)", widget=forms.TextInput(attrs={'class': 'form-control'}))
    batch_name = forms.CharField(max_length=100, required=False, label="Nombre del Lote", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Cupones Navidad'}))

    def generate_coupons(self):
        """
        Genera múltiples cupones según los parámetros del formulario.
        Retorna lista de cupones creados.
        """
        quantity = self.cleaned_data['quantity']
        discount = self.cleaned_data['discount_percentage']
        days = self.cleaned_data['valid_days']
        limit = self.cleaned_data['usage_limit']
        prefix = self.cleaned_data['prefix'] or "GEN"
        
        created_coupons = []
        now = timezone.now()
        valid_to = now + timezone.timedelta(days=days)
        
        for _ in range(quantity):
            # Generar código aleatorio único
            random_str = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
            code = f"{prefix}-{random_str}"
            
            # Asegurar unicidad del código
            while Coupon.objects.filter(code=code).exists():
                random_str = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
                code = f"{prefix}-{random_str}"
            
            coupon = Coupon.objects.create(
                code=code,
                discount_percentage=discount,
                valid_from=now,
                valid_to=valid_to,
                usage_limit=limit,
                active=True
            )
            created_coupons.append(coupon)
            
        return created_coupons
