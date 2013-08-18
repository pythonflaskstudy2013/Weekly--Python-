#!/usr/bin/env python
from flask import Flask
from flask import render_template, render_template_string, request

app = Flask(__name__)

books = ['Programming in Scala', 'Mining the Social Web', 'Pattern-Oriented Software Architecture']

@app.route('/inherit')
def inherit():
	return render_template('child.html')

@app.route('/books')
def list():
	return render_template('books.html', books=books)

@app.route('/animals')
def animals():
	return render_template('animals.html', animals=[
		'cat', 'dog', 'pig', 'cow', 'sheep', 'panda', 'bear'
	])

@app.route('/macro')
def forms():
	return render_template('macro.html')

@app.route('/filter')
def filter():
	return render_template('filter.html')

app.run(debug=True)
