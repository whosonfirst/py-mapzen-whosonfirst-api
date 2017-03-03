import flamework.api.client

class Mapzen(flamework.api.client.OAuth2):

    def __init__(self, api_key, **kwargs):
        
        if not kwargs.get('hostname', None):
            kwargs['hostname'] = 'whosonfirst-api.mapzen.com'

        if not kwargs.get('endpoint', None):
            kwargs['endpoint'] = '/'

        self.api_key = api_key
        
        flamework.api.client.OAuth2.__init__(self, None, **kwargs)    
        
    def set_auth(self, kwargs):
        kwargs['api_key'] = self.api_key
    
class OAuth2(flamework.api.client.OAuth2):

    def __init__(self, access_token, **kwargs):

        if not kwargs.get('hostname', None):
            kwargs['hostname'] = 'whosonfirst-api.mapzen.com'

        if not kwargs.get('endpoint', None):
            kwargs['endpoint'] = '/'

        flamework.api.client.OAuth2.__init__(self, access_token, **kwargs)
