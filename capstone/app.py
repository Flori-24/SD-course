from flask import Flask, jsonify, request
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


@app.route('/api/quizzes', methods=['GET'])
@cross_origin(origins= '*') 
def get_quizzes():
    connection = create_connection()
    cur = connection.cursor(dictionary=True)
    cur.execute('''SELECT * from quizzes''')
    quizzes = cur.fetchall()
    cur.close()
    connection.close() 
    return jsonify(quizzes)


@app.route('/api/quizzes', methods=['POST'])
@cross_origin(origins= '*') 
def post_quizzes():
    connection = create_connection()
    cur = connection.cursor(dictionary=True)
    title = request.json['title']
    description = request.json['description']
    cur.execute("INSERT INTO quizzes (title, description) VALUES (%s, %s)", (title, description))
    connection.commit()
    cur.close()
    connection.close() 
    return jsonify({"message": "Quiz created successfully!"})


@app.route('/api/quizzes/<int:quiz_id>', methods=['GET'])
@cross_origin(origins='*') 
def get_quiz_by_id(quiz_id):
    connection = create_connection()
    cur = connection.cursor(dictionary=True)
    cur.execute('''SELECT * from quizzes where id = %s''', (quiz_id,))
    quiz = cur.fetchall()
    cur.close()
    connection.close() 
    return jsonify(quiz)

@app.route('/api/quizzes/<int:quiz_id>', methods=['PUT'])
@cross_origin(origins='*') 
def update_quiz_by_id(quiz_id):
    connection = create_connection()
    cur = connection.cursor(dictionary=True)
    title = request.json['title']
    description = request.json['description']
    cur.execute("UPDATE quizzes SET title = %s, description = %s WHERE id = %s",  (title, description, quiz_id))
    connection.commit()
    cur.close()
    connection.close() 
    return jsonify({"message": "Quiz updated successfully!"})


@app.route('/quizzes/<int:quiz_id>', methods=['DELETE'])
@cross_origin(origins='*') 
def delete_quiz_by_id(quiz_id):
    connection = create_connection()
    cur = connection.cursor(dictionary=True)
    cur.execute("DELETE from quizzes where id = %s", (quiz_id,))
    connection.commit()
    cur.close()
    connection.close() 
    return jsonify({"message": "Quiz deleted successfully!"})

@app.route('/api/quizzes/<int:quiz_id>/questions', methods=['GET'])
@cross_origin(origins='*')
def get_quiz_questions(quiz_id):
    connection = create_connection()
    cur = connection.cursor(dictionary=True)
    cur.execute('''SELECT id as question_id, question_text from questions where quiz_id = %s''', (quiz_id,))
    questions = cur.fetchall()
    result = []
    for question in questions:
        cur.execute('''SELECT id as choice_id, choice_text, is_correct from choices where question_id = %s''', (question['question_id'],))
        choices = cur.fetchall()
        formatted_question = {
            "question_id": question['question_id'], 
            "question_text": question['question_text'], 
            "choices": [
                {"choice_id": choice["choice_id"], "choice_text": choice["choice_text"], "is_correct": choice["is_correct"]}
                for choice in choices  
            ]
        }
        result.append(formatted_question)  
    cur.close()  
    connection.close()  
    return jsonify(result) 


@app.route('/api/submit', methods=['POST'])
@cross_origin(origins='*')
def post_data():
    connection = create_connection()
    cur = connection.cursor(dictionary=True) 
    answers = request.json['answers']
    score = 0
    for answer in answers:
        question_id = answer['question_id']
        choice_id = answer['choice_id']
        cur.execute("SELECT is_correct FROM choices WHERE id = %s AND question_id = %s", (choice_id, question_id))
        result = cur.fetchone()
        print(f"Result for question_id {question_id} and choice_id {choice_id}: {result}")  
        if result and result['is_correct']:
            score += 1
    cur.close()  
    connection.close()  
    return jsonify({"score": score})

if __name__ == '__main__':
    app.run(port=5000)