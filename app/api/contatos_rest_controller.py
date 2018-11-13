"""
Este é o módulo suporta todas as ações de REST para o objeto Contatos
"""
from datetime import datetime
from flask import (make_response, abort)

from app.db.contatos_db import ContatosDb

class ContatosRestController(object):

    def __init__():
        print("Constructor [ContatosRestController]")
    

    def buscar_todos_os_contatos():
        """
        Retorna lista com todos os contatos.
        :return: json
        """
        db = ContatosDb()
        return db.buscar_todos_os_contatos(), 200

    def buscar_contatos_por_id(contato_id):

        db = ContatosDb()
        return db.buscar_contatos_por_id(contato_id)

    def criar_contato(contato):

        db = ContatosDb()
        
        id = contato.get('id', None)
        nome = contato.get('nome', None)
        canal = contato.get('canal', None)
        obs = contato.get('obs', None)
        valor = contato.get('valor', None)

        if id is not None and nome is not None:
            novo_contato = {
                'id': id,
                'nome': nome,
                'canal': canal,
                'obs': obs,
                'valor': valor
            }
            return db.criar_contato(novo_contato), 201
        else:
            abort(406, 'Id e nome não informados {http}'.format(http='(Error)'))

    def atualizar_contato(contato_id, contato):
        db = ContatosDb()
        return db.atualizar_contato(contato)

    def deletar_contato(contato_id):
        """
        Usado para remover objeto Contato da base

        :param contato_id:      last name of person to delete
        :return:                200 quando removido, 404 se não foi encontrado
        """
        db = ContatosDb()
        contato_retorno = db.deletar_contato(contato_id)
        if contato_retorno == 1:
            return make_response('Contato com o id {contato_id} removido com sucesso'.format(contato_id=contato_id), 200)

        # Otherwise, nope, person to delete not found
        else:
            abort(404, 'Contato com o id {contato_id} não foi encontrado'.format(contato_id=contato_id))
