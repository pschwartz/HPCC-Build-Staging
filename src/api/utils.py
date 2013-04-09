class Registry(object):
    @staticmethod
    def register_get(api, view, endpoint, url, pk='id', pk_type='int'):
        view_func = view.as_view(endpoint)
        api.add_url_rule(url, defaults={pk: None},
                         view_func=view_func, methods=['GET', ])
        api.add_url_rule('%s<%s:%s>' % (url, pk_type, pk), view_func=view_func,
                         methods=['GET', ])

    @staticmethod
    def register_put(api, view, endpoint, url, pk='id', pk_type='int'):
        view_func = view.as_view(endpoint)
        api.add_url_rule('%s<%s:%s>' % (url, pk_type, pk), view_func=view_func,
                         methods=['PUT', ])

    @staticmethod
    def register_delete(api, view, endpoint, url, pk='id', pk_type='int'):
        view_func = view.as_view(endpoint)
        api.add_url_rule('%s<%s:%s>' % (url, pk_type, pk), view_func=view_func,
                         methods=['DELETE', ])

    @staticmethod
    def register_post(api, view, endpoint, url, pk='id', pk_type='int'):
        view_func = view.as_view(endpoint)
        api.add_url_rule(url, view_func=view_func, methods=['POST', ])

    @staticmethod
    def register_api(api, view, endpoint, url, pk='id', pk_type='int'):
        Registry.register_get(api, view, endpoint, url, pk, pk_type)
        Registry.register_put(api, view, endpoint, url, pk, pk_type)
        Registry.register_delete(api, view, endpoint, url, pk, pk_type)
        Registry.register_post(api, view, endpoint, url, pk, pk_type)
