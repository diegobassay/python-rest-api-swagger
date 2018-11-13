from tinydb import TinyDB, Query
import os

class ContatosDb(object):

	def __init__(self):
		pathContatos = os.path.normpath(os.path.join(os.path.dirname(__file__), '../contatos-db.json'))
		self.db = TinyDB(pathContatos)

		if not pathContatos or str(self.db.table('contatos').all()) == '[]':
			tbContatos = self.db.table('contatos')
			tbContatos.insert({ 'id': 1, 'nome': 'Diego Bassay', 'canal': 'email', 'valor': 'diegobassay@gmail.com', 'obs': 'Email do Diego'})
			tbContatos.insert({ 'id': 2, 'nome': 'Luke Skywalker', 'canal': 'telefone', 'valor':'990907654', 'obs': 'Telefone do Luke'})
			tbContatos.insert({ 'id': 3, 'nome': 'Darth Vader', 'canal': 'fixo', 'valor':'34345678', 'obs': 'Telefone da Casa do Vader'})
			tbContatos.insert({ 'id': 4, 'nome': 'Han Solo', 'canal': 'email', 'valor':'harisonford@yahoo.com', 'obs': 'Email do Han Solo'})
			tbContatos.insert({ 'id': 5, 'nome': 'Mestre Yoda', 'canal': 'email', 'valor':'yoda@jedi.com', 'obs': 'Email do Mestre Yoda'})
			tbContatos.all()

	def buscar_todos_os_contatos(self):
		return self.db.table('contatos').all()

	def buscar_contatos_por_id(self, idContato):
		QueryContato = Query()
		return self.db.table('contatos').search(QueryContato.id == int(idContato))

	def criar_contato(self, Contato):
		self.db.table('contatos').insert(Contato)
		return Contato

	def deletar_contato(self, idContato):
		QueryContato = Query()
		contato = self.db.table('contatos').search(QueryContato.id == int(idContato))

		if str(contato) == '[]':
			statusOp = 0
		else:
			self.db.table('contatos').remove(QueryContato.id == int(idContato))
			print(self.db.all())
			statusOp = 1

		return statusOp

	def atualizar_contato(self, Contato):
		
		QueryContato = Query()
		SearchContato = self.db.table('contatos').search(QueryContato.id == int(Contato['id']))
		statusOp = None
		
		if str(SearchContato) == '[]':
			statusOp = 0
		else:
			self.db.table('contatos').update({'nome': Contato['nome']}, QueryContato.id == int(Contato['id']))
			statusOp = 1

		return statusOp
