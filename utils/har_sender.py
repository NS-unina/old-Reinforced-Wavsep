from copy import deepcopy
import json
import sys

import requests

# from haralyzer import HarParser, HarPage
from my_har_parser import HarParser


methods = {
    "GET": requests.get,
    "POST": requests.post,
    "PUT": requests.put,
    "DELETE": requests.delete
}

def default_headers():
    return {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:69.0) Gecko/20100101 Firefox/69.0"}

class HttpRequest:
    def __init__(self, url: str, method: str = "GET", path: str = "/", headers={}, params={}, proxy=""):
        self.url = url
        self.method = method
        self.path = path
        # HttpHeader
        self.headers = {**deepcopy(headers), **default_headers()}
        # If method is post, define the GET
        self.params = deepcopy(params)
        self.proxy = proxy

    def set_proxy(self, host, port):
        self.proxy = "http://{}:{}".format(host, port)


    @staticmethod
    def get(url, path="/", headers={}, params={}):
        return HttpRequest(url, "GET", path, headers, params)

    @staticmethod
    def post(url, path="/", headers={}, params={}):
        return HttpRequest(url, "POST", path, headers, params)

    @staticmethod
    def put(url, path="/", headers={}, params={}):
        return HttpRequest(url, "PUT", path, headers, params)

    @staticmethod
    def delete(url, path="/", headers={}, params={}):
        return HttpRequest(url, "DELETE", path, headers, params)

    def send(self):
        req_function = methods[self.method]
        if self.method == "POST":
            resp = req_function(self.url + self.path, proxies = {"http" : self.proxy, "https" : self.proxy}, verify = False, data = self.params, headers = self.headers)
        else: 
            resp = req_function(self.url + self.path, proxies = {"http" : self.proxy, "https" : self.proxy}, verify = False, params = self.params, headers = self.headers)
        return resp


    def add_header(self, name, value):
        if (self.contains_header(name)):
            raise Exception("Duplicate Param")
        self.headers[name] = value
        return self

    def add_param(self, name, value, in_query_string):
        # TBD = same param in query and in body
        self.params[name] = value
        return self


    def to_dict(self):
        return {
            "url": self.url,
            "method": self.method,
            "path": self.path,
            "headers": self.headers,
            "params" : self.params
        }

    def to_json(self):
        return json.dumps(self.to_dict(), indent=4)

    def __str__(self):
      return str(self.to_dict())
        # return """POST {}\nHost: {}\n{}\n{}""".format(self.path, urlparse(self.url).netloc, self.headers_to_str(), self.params_to_str())


json_obj = []

def to_dict(l: list):
    """Generate a dictionary from an array

    Args:
        l (list): A list 

    Returns:
        dict: A dictionary
    """
    ret = {}
    for i in l:
        ret[i['name']] = i['value']
    return ret

def send_har_entry(req, proxy):
    req_function = methods[req.method]
    if req.method == "POST":
        print(req.text)
        # resp = req_function(req.url , proxies = {"http" : proxy, "https" : proxy}, verify = False, data = req.params, headers = to_dict(req.headers))
    # else: 
    #     resp = req_function(req.url, proxies = {"http" : proxy, "https" : proxy}, verify = False, headers = to_dict(req.headers))
    # return resp


def send_from_har(har_file, proxy):
    requests = HarParser.from_file(har_file)
    print(requests)
    # the_page = har_parser.pages[0]
    # for entry in the_page.entries:
    #     req = entry.request
    #     # print("Send {}".format(req.url))
    #     send_har_entry(req, proxy)

