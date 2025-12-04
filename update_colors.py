import re

with open('Commercefy/appCommercefy/models.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Buscar y reemplazar la sección de Apariencia
old_pattern = r'    # Apariencia\n.*?    # Redes Sociales'
new_text = '''    # Apariencia - Fondos
    bg_body = models.CharField(max_length=7, default="#F8F9FA", verbose_name="Fondo Body", help_text="Formato HEX")
    bg_surface = models.CharField(max_length=7, default="#FFFFFF", verbose_name="Fondo Superficie", help_text="Formato HEX")
    bg_soft = models.CharField(max_length=7, default="#F5F5F5", verbose_name="Fondo Suave", help_text="Formato HEX")
    
    # Apariencia - Colores Primarios
    primary_color = models.CharField(max_length=7, default="#3b84f8", verbose_name="Color Primario", help_text="Formato HEX (ej: #3b84f8)")
    primary_color_dark = models.CharField(max_length=7, default="#276adf", verbose_name="Color Primario Oscuro", help_text="Formato HEX")
    primary_color_light = models.CharField(max_length=7, default="#5789e7", verbose_name="Color Primario Claro", help_text="Formato HEX")
    
    # Apariencia - Colores Secundarios
    secondary_color = models.CharField(max_length=7, default="#9df38b", verbose_name="Color Secundario", help_text="Formato HEX (ej: #9df38b)")
    secondary_color_dark = models.CharField(max_length=7, default="#82e76c", verbose_name="Color Secundario Oscuro", help_text="Formato HEX")
    
    # Apariencia - Acentos
    accent_color = models.CharField(max_length=7, default="#FFD6A5", verbose_name="Color de Acentos", help_text="Formato HEX")
    accent_color_dark = models.CharField(max_length=7, default="#FFC085", verbose_name="Color de Acentos Oscuro", help_text="Formato HEX")
    
    # Apariencia - Estado
    danger_color = models.CharField(max_length=7, default="#ed6464", verbose_name="Color Peligro", help_text="Formato HEX")
    danger_color_dark = models.CharField(max_length=7, default="#f35050", verbose_name="Color Peligro Oscuro", help_text="Formato HEX")
    warning_color = models.CharField(max_length=7, default="#FFD93D", verbose_name="Color Advertencia", help_text="Formato HEX")
    info_color = models.CharField(max_length=7, default="#9BF6FF", verbose_name="Color Información", help_text="Formato HEX")
    success_color = models.CharField(max_length=7, default="#CAFFBF", verbose_name="Color Éxito", help_text="Formato HEX")
    
    # Apariencia - Texto
    text_main = models.CharField(max_length=7, default="#2D3436", verbose_name="Texto Principal", help_text="Formato HEX")
    text_muted = models.CharField(max_length=7, default="#636E72", verbose_name="Texto Silenciado", help_text="Formato HEX")
    text_light = models.CharField(max_length=7, default="#B2BEC3", verbose_name="Texto Claro", help_text="Formato HEX")
    
    # Legacy colors (para compatibilidad)
    button_hover_color = models.CharField(max_length=7, default="#2c5cc0", verbose_name="Color Hover de Botones", help_text="Formato HEX (ej: #2c5cc0)")
    background_color = models.CharField(max_length=7, default="#ffffff", verbose_name="Color de Fondo Legado", help_text="Formato HEX (ej: #ffffff)")
    
    # Redes Sociales'''

content = re.sub(old_pattern, new_text, content, flags=re.DOTALL)

with open('Commercefy/appCommercefy/models.py', 'w', encoding='utf-8') as f:
    f.write(content)

print('✓ Actualización completada')
