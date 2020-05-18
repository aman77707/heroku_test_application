import os
from flask import Flask, request, abort, jsonify, json
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, Question

QUESTIONS_PER_PAGE = 10


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)

    '''
    Set up CORS. Allow '*' for origins.
    '''
    CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)
    
    def updateField(field, jsonObj ,jsonKey):
        return field if jsonObj.get(jsonKey, None) is None else jsonObj.get(jsonKey)

    '''
    Use the after_request decorator to set Access-Control-Allow
    '''
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'GET, POST,  PATCH , DELETE, OPTIONS')
        return response

    @app.route('/questions', methods=['POST'])
    def post_question():
    	print("Hitting POST")                                                                                                                           
    	data = request.get_json()
    	question = data.get('question', None)
    	answer = data.get('answer', None)
    	category = data.get('category', None)
    	difficulty = data.get('difficulty', None)

    	print ("Got the values ")
    	
    	try:
    		question = Question(question=question, answer=answer, category=category, difficulty=difficulty)
    		question.insert()
    	except:
    		abort(422)

    	return "Hello and Welcome to the heroku deployment test application!. Your record was successfully inserted!"


    @app.route('/questions', methods=['GET'])
    def get_questions():
    	print("Hitting GET")
    	questions = Question.query.all()

    	if questions is None:
    		return "Sorry!! No records found"
    	return jsonify({
    		"success" : True,
    		"questions" : [q.format() for q in questions]
    		})

    '''
    Create error handlers for all expected errors 
    including 404 and 422. 
    '''
     
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False, 
            "error": 404,
            "message": "Resource not found"
            }), 404

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False, 
            "error": 422,
            "message": "Unprocessable"
            }), 422

    @app.errorhandler(405)
    def method_not_allowed(error):
        return jsonify({
            "success": False, 
            "error": 405,
            "message": "Method not allowed"
            }), 405

    @app.errorhandler(400)
    def not_found(error):
        return jsonify({
            "success": False, 
            "error": 400,
            "message": "Bad request"
            }), 400

    return app

app = create_app()
if __name__ == '__main__':
    app.run()

    
