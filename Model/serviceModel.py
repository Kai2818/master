from typing import Optional

class ApiModel:
    def __init__(self, id, service, host, token, secret, routeName, path, method, desc):
        self.id = id
        self.service = service
        self.host = host
        self.token = token
        self.secret = secret
        self.routeName = routeName
        self.path = path
        self.method = method
        self.desc = desc

        # id: Optional[int]
        # service: Optional[str]
        # host: Optional[str]
        # token: Optional[str]
        # secret: Optional[str]
        # routeName: Optional[str]
        # path: Optional[str]
        # method: Optional[str]
        # desc: Optional[str]