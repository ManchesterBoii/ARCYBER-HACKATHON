from werkzeug.wsgi import DispatcherMiddleware
from werkzeug.serving import run_simple

from frontend import flask_app
from backend1 import URIPathVis


application = DispatcherMiddleware(flask_app, {
    '/URIPathVis': URIPathVis.server,
})



if __name__ == '__main__':
    run_simple('localhost', 8050, application)