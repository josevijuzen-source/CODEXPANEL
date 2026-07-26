# -*- coding: utf-8 -*-
from .views import VERSION, BUILD

def version_context(request):
    """Add version information to all templates"""
    return {
        'CODEXPANEL_VERSION': VERSION,
        'CODEXPANEL_BUILD': BUILD,
        'CODEXPANEL_FULL_VERSION': f"{VERSION}.{BUILD}"
    }

def cosmetic_context(request):
    """Add cosmetic data (custom CSS) to all templates"""
    try:
        from .models import CodexPanelCosmetic
        cosmetic = CodexPanelCosmetic.objects.get(pk=1)
        return {
            'cosmetic': cosmetic
        }
    except:
        from .models import CodexPanelCosmetic
        cosmetic = CodexPanelCosmetic()
        cosmetic.save()
        return {
            'cosmetic': cosmetic
        }