import os

from flask import Flask

from flask import request

from flask import render_template

todo_store = {}

todo_store['shivang'] =  ['Go for run','Listen Music']
todo_store['raj'] = ['Play','Enjoy']
todo_store['depo'] = ['Eat', 'Code']
todo_store['sanket'] = ['Sleep','Code']
todo_store['aagam'] = ['Play Cricket', 'Have Tea']

def create_app(test_configuration=None):
	app=Flask(__name__, instance_relative_config=True)

	try:
		os.makedirs(app.instance_path)
	except OSError:
		pass

	def select_todos(name):
		global todo_store
		return todo_store[name]

	# def todo_view(mytodo):			#Views : Representation
	# 	x='List of my ToDos'+'<br>'
	# 	for y in mytodo:
	# 		x+=y+'<br>'

	# 	return x	

	def insert_todos(name,todo):
		global todo_store
		current_todos = todo_store[name]
		current_todos.append(todo)
		todo_store[name] = current_todos
		return

	def add_todo_by_name(name,todo):
		#Call DB Function
		insert_todos(name,todo)
		return

	def get_todos_by_name(name):	#Model: DB
		try:
			return select_todos(name)
		except:
			return None	

		return select_todos(name)

	#http://127.0.0.1:5000/todos?name=duster
	@app.route('/todos')
	def todos():					#Controller : Request Passing & Connecting Components		(MVC)
		name=request.args.get('name');
		print('----------')
		print(name)
		print('----------')
		
		person_todo_list=get_todos_by_name(name)
		#return todo_view(person_todo_list)
		
		if(person_todo_list==None):
			#throw 404
			return render_template('404.html'), 404
		else:
			return render_template('todo_view.html',todos=person_todo_list)	#filename, variable		#jinja templating

	@app.route('/add_todos')
	def add_todos():
		name = request.args.get('name')
		todo = request.args.get('todo')
		
		add_todo_by_name(name,todo)

		return 'Added Successfully'

	@app.route('/delete_todos')
	def delete_todos():
		name = request.args.get('name')
		todo = request.args.get('todo')
		

		return 'Deleted Successfully'		


	# @app.route('/shivang')	#linking to function
	# def shivang():
	# 	mytodo=['Go for run','Listen Music']
	# 	return todo_view(mytodo)	#returning HTML
	
	# @app.route('/raj')	#linking to function
	# def raj():
	# 	mytodo=['Play','Enjoy']
	# 	return todo_view(mytodo)

	return app