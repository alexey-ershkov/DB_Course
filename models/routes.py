class Routes:
    def __init__(self):
        self.__routes = [
            {'name': 'Составить отчет о банкетах в марте 2017 года', 'href': 'first', 'active': False},
            {'name': 'Составить отчет о работе менеджеров в марте 2017', 'href': 'second', 'active': False},
            {'name': 'Показать все сведения о самом молодом менеджере', 'href': 'third', 'active': False},
            {
                'name': 'Показать сведения о менеджерах, которые пока не обслуживали ни один банкет, которые не '
                        'приняли ни одного заказа', 'href': 'forth', 'active': False},
            {'name': 'Показать сведения о менеджерах, не принявших ни одного заказа в марте 2013 года', 'href': 'fifth',
             'active': False},
            {'name': 'Показать сведения о зале, который чаще всех заказывали в 2017', 'href': 'sixth', 'active': False},
        ]

    @property
    def links(self):
        return self.__routes

    def set_active(self, route_name):
        for route in self.__routes:
            if route["href"] == route_name:
                route.update(active=True)
            else:
                if route["active"]:
                    route.update(active=False)

    def clear(self):
        for route in self.__routes:
            if route["active"]:
                route.update(active=False)