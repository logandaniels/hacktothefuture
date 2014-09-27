import web
from structure import dataModel, product, pro_con
import json

web.config.debug = False

urls = (
	'/', 'index',
	'/products/(\d+)', 'prod',

	# GETs
	'/products/(\d+)/gettoppros=(\d+)', 'gettoppros',
	'/products/(\d+)/gettopcons=(\d+)', 'gettopcons',
	'/products/(\d+)/getpros', 'getpros',
	'/products/(\d+)/getcons', 'getcons',

	# POSTs
	'/products/(\d+)/addpro_message=(.+)', 'addpro',
	'/products/(\d+)/addcon_message=(.+)', 'addcon',
	'/products/(\d+)/voteup_proconid=(\d+)', 'voteup',
	'/products/(\d+)/votedown_proconid=(\d+)', 'votedown'
	'/saveVals', 'save'
	)

# serve html pages

class index:
	def GET(self):
		render = web.template.render('./')    
		return render.index()

class prod:
	def GET(self, prodID):
		render = web.template.render('./')
		return render.product(prodID)


# GETs

class gettoppros:
	def GET(self, prod_id, n):
		if (model.productList.get(int(prod_id),-1) ==-1):
			return ""
		return json.dumps(model.productList[int(prod_id)].getTopPros(int(n)), default=lambda o: o.__dict__)

class gettopcons:
	def GET(self, prod_id, n):
		if (model.productList.get(int(prod_id),-1) ==-1):
			return ""
		return json.dumps(model.productList[int(prod_id)].getTopCons(int(n)), default=lambda o: o.__dict__)

class getpros:
	def GET(self, prod_id):
		if (model.productList.get(int(prod_id),-1) ==-1):
			return ""
		return json.dumps(model.productList[int(prod_id)].getPros(), default=lambda o: o.__dict__)

class getcons:
	def GET(self, prod_id):
		if (model.productList.get(int(prod_id),-1) ==-1):
			return ""
		return json.dumps(model.productList[int(prod_id)].getCons(), default=lambda o: o.__dict__)

# POSTs

class addpro:
	def POST(self, prod_id, message):
		model.productList[int(prod_id)].addPro(message)
class addcon:
	def POST(self, prod_id, message):
		model.productList[int(prod_id)].addCon(message)

class voteup:
	def POST(self, prod_id, pcID):
		model.productList[int(prod_id)].voteUp(int(pcID))

class votedown:
	def POST(self, prod_id, pcID):
		model.productList[int(prod_id)].voteDown(int(pcID))



if __name__ == "__main__": 
	model = dataModel()
	app = web.application(urls, globals())
	app.run()
