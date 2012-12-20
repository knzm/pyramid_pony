import base64
import zlib

from pyramid.response import Response

from .pony import PONY, UNICORN, TEMPLATE


def decode(data):
    data = base64.b64decode(data)
    return zlib.decompress(data).decode('ascii')


def pony_view(request):
    home = request.script_name or "/"
    link = "add horn!"
    url = request.path + "?horn=1"
    animal = decode(PONY)
    html = TEMPLATE.format(animal=animal, url=url, link=link, home=home)
    return Response(html)


def unicorn_view(request):
    home = request.script_name or "/"
    link = "remove horn!"
    url = request.path
    animal = decode(UNICORN)
    html = TEMPLATE.format(animal=animal, url=url, link=link, home=home)
    return Response(html)


class HornPredicate(object):
    def __init__(self, val, config):
        self.val = val

    def text(self):
        return 'content_type = %s' % (self.val,)

    phash = text

    def __call__(self, context, request):
        return bool(request.params.get("horn")) == bool(self.val)


def includeme(config):
    config.add_route("pony", "/pony")
    config.add_view_predicate('horn', HornPredicate)
    config.add_view(pony_view, route_name="pony", horn=False)
    config.add_view(unicorn_view, route_name="pony", horn=True)
