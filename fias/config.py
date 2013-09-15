#coding: utf-8
from __future__ import unicode_literals, absolute_import

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

_DEFAULT = ('landmark', 'houseint', 'house')

FIAS_TABLES = ['socrbase', 'normdoc', 'addrobj']
FIAS_TABLES.extend([x.lower() for x in list(getattr(settings, 'FIAS_TABLES', _DEFAULT)) if x.lower() in _DEFAULT])

FIAS_DELETED_TABLES = ('addrobj', 'house', 'houseint', 'normdoc')

FIAS_DATABASE_ALIAS = getattr(settings, 'FIAS_DATABASE_ALIAS', 'fias')

FIAS_SEARCHERS = {
    'sequence': 'step_by_step',
    'sphinx': 'by_sphinx',
}

_s = getattr(settings, 'FIAS_SEARCH_ENGINE', 'sequence')

FIAS_SEARCH_ENGINE = _s if _s in FIAS_SEARCHERS else 'sequence'

if FIAS_SEARCH_ENGINE == 'sphinx':
    try:
        import sphinxit
    except ImportError:
        raise ImproperlyConfigured('sphinxit module required for `sphinx` search engine!')

    FIAS_SPHINX_ADDROBJ_INDEX_NAME = getattr(settings, 'FIAS_SPHINX_ADDROBJ_INDEX_NAME', 'addrobj')

    FIAS_SPHINX_ADDROBJ_INDEX = FIAS_DATABASE_ALIAS + '_' + FIAS_SPHINX_ADDROBJ_INDEX_NAME

FIAS_SUGGEST_VIEW = 'fias:suggest_{}'.format(FIAS_SEARCHERS[FIAS_SEARCH_ENGINE])

# Чтобы использовать для данных ФИАС другую базу данных,
# добавьте роутер 'fias.routers.FIASRouter' в список `DATABASE_ROUTERS`