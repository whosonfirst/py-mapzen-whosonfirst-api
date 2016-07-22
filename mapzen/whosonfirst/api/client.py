import flamework.api.client

class OAuth2(flamework.api.client.OAuth2):

    def __init__(self, access_token, **kwargs):

        if not kwargs.get('hostname', None):
            kwargs['hostname'] = 'whosonfirst.mapzen.com'

        if not kwargs.get('endpoint', None):
            kwargs['endpoint'] = '/api/rest/'

        flamework.api.client.OAuth2.__init__(self, access_token, **kwargs)
