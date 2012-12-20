from .pony import view as pony_view


def pony_tween_factory(handler, registry):
    def pony_tween(request):
        if request.path == '/pony':
            return pony_view(request)
        else:
            return handler(request)
    return pony_tween


def includeme(config):
    config.add_tween('pyramid_pony.tween.pony_tween_factory')
