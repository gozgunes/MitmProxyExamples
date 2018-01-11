import base64
import re
from credentials import *

def request(flow):
    hostname = flow.request.pretty_host
    data = flow.request.content.decode('utf-8')

    if hostname.endswith("api.x.com"):
        auth = b64encode(X_USERNAME).decode('utf-8') + ':' + b64encode(X_PASSWORD).decode('utf-8')
        flow.request.headers["Authorization"] = "Basic " + b64encode(auth).decode('utf-8')

    if hostname.endswith("x.com"):
        data = re.sub('<a1:Username>(.*)<\/a1:Username>', '<a1:Username>' + X_USERNAME + '</a1:Username>', data)
        data = re.sub('<a1:Password>(.*)<\/a1:Password>', '<a1:Password>' + X_USERNAME + '</a1:Password>', data)

        flow.request.content = data.encode('utf-8')

def b64encode(s):
    return base64.b64encode(s.encode('utf-8'))

def error(flow):
    flow.response = HTTPResponse.make(404, b"we encountered an error while inserting credentials",
                                      {"Content-Type": "text/html"})

def finish(flow):
    flow.response = HTTPResponse.make(200, flow, {"Content-Type": "text/html"})
