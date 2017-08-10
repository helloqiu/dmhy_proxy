# -*- coding: utf-8 -*-

import requests
from flask import Flask, Response, request
from logger import logger, enable_pretty_logging
from gevent.wsgi import WSGIServer

app = Flask(__name__)
enable_pretty_logging(logger)
proxies = {'http': 'socks5://localhost:1080'}
base_url = 'http://share.dmhy.org/{}'


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def handler(path):
    logger.info('Get path "{}".'.format(request.full_path))
    r = requests.get(base_url.format(request.full_path), proxies=proxies)
    return Response(r.content, mimetype="text/xml")


http_server = WSGIServer(('0.0.0.0', 9999), app)
http_server.serve_forever()
