from flask import Flask, jsonify
import os


app = Flask(__name__)

# ============= Chaos Middleware ==================
# from pdchaos.middleware.contrib.flask.flask_middleware import FlaskMiddleware
#
# app.config['CHAOS_MIDDLEWARE_APPLICATION_NAME'] = os.environ['CHAOS_MIDDLEWARE_APPLICATION_NAME']
# app.config['CHAOS_MIDDLEWARE_APPLICATION_ENV'] = os.environ['CHAOS_MIDDLEWARE_APPLICATION_ENV']
# app.config['CHAOS_MIDDLEWARE_PROOFDOCK_API_TOKEN'] = os.environ['CHAOS_MIDDLEWARE_PROOFDOCK_API_TOKEN']
#
# middleware = FlaskMiddleware(app)


@app.route("/")
def recommendations():
    return "Hello World"


if __name__ == "__main__":
    app.run()