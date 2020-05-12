import cherrypy


class HelloWorld(object):
    @cherrypy.expose
    def index(self):
        return "hi world?"


if __name__ == '__main__':
    cherrypy.quickstart(HelloWorld())
