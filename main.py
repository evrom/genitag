from bottle import Bottle
from configuration import config
from urls import setup_routing
port = config['app']['port']
host = config['app']['host']
development_mode = config['app']['development_mode']
app = Bottle()
setup_routing(app)
if development_mode:
    from bottle import static_file

    @app.route('/static/<filename:path>')
    def server_static(filename):
        return static_file(filename, root='./static/')

    @app.route('/docs/<filename:path>')
    def docs_static(filename):
        return static_file(filename, root='./docs/_build/html/')

if __name__ == '__main__':
    app.run(server='waitress', host=host, port=port,
            debug=development_mode, reloader=development_mode)
