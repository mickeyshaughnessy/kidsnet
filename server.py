# The kidsnet API
# gunicorn -k gevent -t 600 -b 0.0.0.0:8010 -w 8 -p /tmp/server.pid server:app
# -k: worker_type, -t: startup grace period, -b: where to server, -w: number of workers, -p: pid file

import falcon, random, time, glob
from datetime import datetime as dt

from serving.http.handlers.sitter import SitterHandler
from serving.http.handlers.parent import ParentHandler
from serving.http.handlers.signup import SignUpHandler
from serving.http.handers.ping import PingHandler

start = dt.now()
app = falcon.API()

app.add_route('/sitter', SitterHandler())
app.add_route('/parent', ParentHandler())
app.add_route('/new', SignUpHandler())


if __name__ == "__main__":
    from wsgiref import simple_server
    httpd = simple_server.make_server('0.0.0.0', 8010, app)
    httpd.serve_forever()
