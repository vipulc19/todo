import os

from flask import Flask

from flask import request

def create_app(test_configuration=None):
	app=Flask(__name__, instance_relative_config=True)

	try:
		os.makedirs(app.instance_path)
	except OSError:
		pass

	def todo_view(mytodo):			#Views : Representation
		x='List of my ToDos'+'<br>'
		for y in mytodo:
			x+=y+'<br>'

		return x	

	def get_todos_by_name(name):	#Model: DB
		if(name=='shivang'):
			return ['Go for run','Listen Music']
		elif name=='raj':
			return ['Play','Enjoy']
		else:
			mytodo=[]

	#http://127.0.0.1:5000/todos?name=duster
	@app.route('/todos')
	def todos():					#Controller : Request Passing & Connecting Components		(MVC)
		name=request.args.get('name');
		print('----------')
		print(name)
		print('----------')
		
		person_todo_list=get_todos_by_name(name)
		return todo_view(person_todo_list)


	# @app.route('/shivang')	#linking to function
	# def shivang():
	# 	mytodo=['Go for run','Listen Music']
	# 	return todo_view(mytodo)	#returning HTML
	
	# @app.route('/raj')	#linking to function
	# def raj():
	# 	mytodo=['Play','Enjoy']
	# 	return todo_view(mytodo)

	return app
