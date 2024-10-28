from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
from flask_cors import cross_origin
import mysql.connector

app= Flask(__name__)
def create_connection():
    connection = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'Development2426..',
        database = 'e_quizz'
    )
    return connection 
print("Connection to MySQL DB successful")


@app.route('/quizzes', methods=['GET'])
@cross_origin(origins= '*') 
def get_quizzes():
    connection = create_connection()
    cur = connection.cursor(dictionary=True)
    cur.execute('''SELECT * from quizzes''')
    quizzes = cur.fetchall()
    cur.close()
    return jsonify(quizzes)


@app.route('/quizzes', methods=['POST'])
@cross_origin(origins= '*') 
def post_quizzes():
    connection = create_connection()
    cur = connection.cursor(dictionary=True)
    title = request.json['title']
    description = request.json['description']
    cur.execute("INSERT INTO quizzes (title, description) VALUES (%s, %s)", (title, description))
    connection.commit()
    cur.close()
    return jsonify({"message": "Quiz created successfully!"})


@app.route('/quizzes/<int:quiz_id>', methods=['PUT'])
@cross_origin(origins='*') 
def update_quizzes(quiz_id):
    connection = create_connection()
    cur = connection.cursor(dictionary=True)
    title = request.json['title']
    description = request.json['description']
    cur.execute("UPDATE quizzes SET title = %s, description = %s WHERE id = %s",  (title, description, quiz_id))
    connection.commit()
    cur.close()
    return jsonify({"message": "Quiz updated successfully!"})


@app.route('/quizzes/<int:quiz_id>', methods=['DELETE'])
@cross_origin(origins='*') 
def delete_quizzes(quiz_id):
    connection = create_connection()
    cur = connection.cursor(dictionary=True)
    cur.execute("DELETE from quizzes where id = %s", (quiz_id,))
    connection.commit()
    cur.close()
    return jsonify({"message": "Quiz deleted successfully!"})


@app.route('/quizzes/<int:quiz_id>/questions', methods=['GET'])
@cross_origin(origins='*')  
def get_questions(quiz_id):
    connection = create_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * from questions where quiz_id = %s", (quiz_id,))
    questions = cursor.fetchall()
    cursor.close()
    return jsonify(questions)


@app.route('/quizzes/<int:quiz_id>/questions', methods=['POST'])
@cross_origin(origins='*')  
def post_questions(quiz_id):
    connection = create_connection()
    cursor = connection.cursor()
    question_text = request.json['question_text']
    cursor.execute("INSERT INTO questions (quiz_id, question_text) VALUES (%s, %s)", (quiz_id, question_text))
    connection.commit()
    cursor.close()
    return jsonify({"message": "Question added successfully!"})


@app.route('/questions/<int:question_id>/choices', methods=['GET'])
@cross_origin(origins='*')  
def get_choices(question_id):
    connection = create_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * from choices where question_id = %s", (question_id,))
    choices = cursor.fetchall()
    cursor.close()
    return jsonify(choices)


@app.route('/questions/<int:question_id>/choices', methods=['POST'])
@cross_origin(origins='*')  
def post_choices(question_id):
    connection = create_connection()
    cursor = connection.cursor()
    choice_text = request.json['choice_text']
    is_correct = request.json['is_correct']
    cursor.execute("INSERT INTO choices (question_id, choice_text, is_correct) VALUES (%s, %s, %s)", (question_id, choice_text, is_correct))
    connection.commit()
    cursor.close()
    return jsonify({"message": "Choice added successfully!"})


if __name__ == '__main__':
    app.run(port=5000)