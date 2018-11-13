from app.server.http_server import HttpServer

host = 'localhost';
port = 3002;

http_server = HttpServer()
http_server.iniciar(host, port)