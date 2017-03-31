import flamework.api.client

import urllib
import httplib
import logging
import json

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

    # See this - ensure we are GET-ing so that the API key is seen
    # as a GET parameter (20170330/thisisaaronland)

    def execute_method(self, method, kwargs, encode=None):

        logging.debug("calling %s with args %s" % (method, kwargs))

        kwargs['method'] = method
        self.set_auth(kwargs)

        url = self.endpoint
        logging.debug("calling %s" % url)

        url = url + "?" + urllib.urlencode(kwargs)

        conn = httplib.HTTPSConnection(self.hostname)
        conn.request('GET', url)

        rsp = conn.getresponse()
        body = rsp.read()

        logging.debug("response is %s" % body)

        try:
            data = json.loads(body)
        except Exception, e:
            logging.error(e)
            raise Exception, e

        return data

class OAuth2(flamework.api.client.OAuth2):

    def __init__(self, access_token, **kwargs):

        if not kwargs.get('hostname', None):
            kwargs['hostname'] = 'whosonfirst-api.mapzen.com'

        if not kwargs.get('endpoint', None):
            kwargs['endpoint'] = '/'

        flamework.api.client.OAuth2.__init__(self, access_token, **kwargs)
