import json 

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


class Request: 
    def __init__(self, url, method, cookies, headers, body = ""):
        self.url = url
        self.method = method 
        self.cookies = to_dict(cookies)
        self.headers = to_dict(headers)
        self.body = body
# class HarEntry:


class HarParser:
    def from_file(har_file):
        requests = []
        with open(har_file) as f:
            data = json.load(f)

        entries = data['log']['entries']
        for e in entries: 
            req = e['request']
            req_obj = Request(req['url'], req['method'], req['cookies'], req['headers'])
            requests.append(req_obj)
            if req['method'] == "POST":
                req_obj.body = to_dict(req['postData']['params'])

        return requests

