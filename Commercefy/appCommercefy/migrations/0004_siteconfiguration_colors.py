# Generated migration file for new color fields

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appCommercefy', '0003_siteconfiguration_announcement_text_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteconfiguration',
            name='accent_color',
            field=models.CharField(default='#ff6b6b', help_text='Formato HEX (ej: #ff6b6b)', max_length=7, verbose_name='Color de Acentos'),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='button_hover_color',
            field=models.CharField(default='#2c5cc0', help_text='Formato HEX (ej: #2c5cc0)', max_length=7, verbose_name='Color Hover de Botones'),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='text_color',
            field=models.CharField(default='#1a1a1a', help_text='Formato HEX (ej: #1a1a1a)', max_length=7, verbose_name='Color de Texto'),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='background_color',
            field=models.CharField(default='#ffffff', help_text='Formato HEX (ej: #ffffff)', max_length=7, verbose_name='Color de Fondo'),
        ),
    ]
