import urllib2
import urllib
from XmlToDict import XmlDictConfig
from xml.etree import cElementTree as ElementTree



class ApiQuery(object):
    def __init__(self, api_url, api_user, api_pass):
        self.api_url = api_url
        self.api_user = api_user
        self.api_pass = api_pass

    def request(self, **kwargs):
        api_url = self.api_url
        api_user = self.api_user
        api_pass = self.api_pass

        data = urllib.urlencode(kwargs)

        full_url = api_url + '/api?' + data
        password_manager = urllib2.HTTPPasswordMgrWithDefaultRealm()
        password_manager.add_password(None, api_url, api_user, api_pass)
        handler = urllib2.HTTPBasicAuthHandler(password_manager)
        opener = urllib2.build_opener(handler)
        opener.addheaders = [('Content-Type', 'application/x-www-form-urlencoded')]
        urllib2.install_opener(opener)
        data = urllib2.urlopen(full_url, data).read()
        root = ElementTree.XML(data)
        xmldict = XmlDictConfig(root)
        
        return xmldict

if __name__ == "__main__":
    api_url = "http://fridayd.me:7999"
    api_user = "admin"
    api_pass = "goaway"

    api = ApiQuery(api_url, api_user, api_pass)
    print api.request(op="listdjs", name="dj",  seq="420")

