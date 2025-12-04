from .models import Order, SiteConfiguration

def pending_orders_count(request):
    if request.user.is_authenticated and (request.user.is_staff or request.user.groups.filter(name__in=['admin', 'trabajador']).exists()):
        count = Order.objects.filter(estado='Pendiente').count()
        return {'pending_orders_count': count}
    return {}


def site_branding(request):
    try:
        config = SiteConfiguration.objects.first()
    except:
        config = None
    
    if not config:
        return {
            'site_name': 'Multitienda',
            'support_email': 'contacto@multitienda.cl',
            'support_phone': '+56 9 8837 6786',
            'site_logo_url': None,
            'site_config': None
        }
    
    return {
        'site_name': config.site_name,
        'support_email': config.support_email,
        'support_phone': config.support_phone,
        'site_logo_url': config.logo.url if config.logo else None,
        'site_config': config
    }

