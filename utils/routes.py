import json


class Routes:
    def __init__(self):
        with open("dataFiles/menu.json", "r") as menu_raw:
            self.__routes = json.load(menu_raw)

    @property
    def get_routes(self):
        return self.__routes

    def get_url_by_inner_name(self, inner_name):
        for route in self.__routes:
            if route["innerName"] == inner_name:
                return route["url"]
        return None

    def set_active(self, route_name):
        for route in self.__routes:
            if route["url"] == route_name:
                route.update(active=True)
            else:
                if route["active"]:
                    route.update(active=False)

    def clear(self):
        for route in self.__routes:
            if route["active"]:
                route.update(active=False)
