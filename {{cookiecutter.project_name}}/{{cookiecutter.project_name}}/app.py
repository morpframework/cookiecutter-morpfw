import morpfw
from morpfw.authz.pas import DefaultAuthzPolicy
from morpfw.crud import permission as crudperm
import sqlalchemy as sa


class AppRoot(object):
    pass


class App(DefaultAuthzPolicy, morpfw.App):
    pass


@App.path(model=AppRoot, path='/')
def get_approot(request):
    return AppRoot(request)


@App.json(model=AppRoot, permission=crudperm.View)
def index(context, request):
    return {
            'message': 'Hello World'
    }

