import gevent.monkey
gevent.monkey.patch_all()


from flask import Flask
from gevent.pywsgi import WSGIServer
from api.math import math_bp

app = Flask(__name__)
app.register_blueprint(math_bp)

if __name__ == "__main__":
    http_server = WSGIServer(
        ("0.0.0.0", 5001),
        app
    )
    print("Server running on http://0.0.0.0:5001")
    http_server.serve_forever()

