"""
Módulo principal para iniciar o servidor HTTP
"""
from flask import (render_template, request)
import connexion
import os

class HttpServer(object):

    def __init__(self):
        # Criando instancia do connexion
        self.app = connexion.App(__name__)

        # Ler do swaggger.json os endpoints
        self.app.add_api(os.path.normpath(os.path.join(os.path.dirname(__file__), '../api/swagger.json')))

    def stop():
        func = request.environ.get('werkzeug.server.shutdown')
        if func is None:
            raise RuntimeError('')
        func()
        return 'Finalizando servidor'

    def iniciar(self, host, port):   
        print('Servidor iniciado na porta : '+str(port))
        print('Acesse (http://localhost:'+str(port)+'/api/ui) para testar os serviços')
        self.app.run(debug=True,host=host, port=port)