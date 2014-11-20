from bottle import Bottle
from configparser import ConfigParser
from routes import routes
config = ConfigParser()
config.read('./config.ini')
port = config['app']['port']
host = config['app']['host']
development_mode = config['app']['development_mode']
app = Bottle()
for route in routes:
    app.merge(route)
if development_mode:
    from bottle import static_file

    @app.route('/static/<filename:path>')
    def server_static(filename):
        return static_file(filename, root='./static/')

    @app.route('/docs/<filename:path>')
    def docs_static(filename):
        return static_file(filename, root='./docs/_build/html/')

if __name__ == '__main__':
    app.run(host=host, port=port,
            debug=development_mode, reloader=development_mode)