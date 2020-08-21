# exemplo
from flask import Flask, jsonify, request, abort
from api import app

students = [
    {'id': 1, 'name': 'Fulano de Alguem', 'age': 25, 'email': 'ful@mail.com'},
    {'id': 2, 'name': 'Cicrano de Alguem', 'age': 31, 'email': 'cic@mail.com'},
    {'id': 3, 'name': 'Alguem Ja Foi', 'age': 60, 'email': 'alg@mail.com'},
    {'id': 4, 'name': 'Alguem Aqui', 'age': 40, 'email': 'aaqui@mail.com'},
    {'id': 5, 'name': 'Alguem de Alguns', 'age': 20, 'email': 'alal@mail.com'}
]

# HOME PAG
@app.route('/')
def home():
    return 'My flask api Students'

# BEGIN METHODS GET
@app.route('/api/students', methods=['GET'])
def get_students():
    return jsonify({'Students': students})

@app.route('/api/student/<int:student_id>', methods=['GET'])
def get_student_id(student_id):
    for student in students:
        if student['id'] == student_id:
            return jsonify({'Student': student})

    return jsonify({'Student': None})
# END METHODS GET

# BEGIN METHODS POST
@app.route('/api/student', methods=['POST'])
def create_json_student():
    data = request.get_json()

    data['id'] = len(students) + 1
    students.append(data)

    return jsonify({'id': data['id'], 'name': data['name'], 'age': data['age'], 'email': data['email']})
# END METHODS POST

# BEGIN METHODS PUT
@app.route('/api/student', methods=['PUT'])
def put_student():
    data = request.get_json()

    for student in students:
        if student['id'] == data['id']:
            for inf in data:
                if data[inf] != student[inf]:
                    student[inf] = data[inf]

            return jsonify({'Student': student})
    return jsonify({'Student': None})
# END METHODS PUT
    
# BEGIN METHOD DELETE
@app.route('/api/student/<int:student_id>', methods=['DELETE'])
def del_student(student_id):
    cont = 0
    for student in students:
        if student['id'] == student_id:
            msg = jsonify({'Student deleted': student})
            del(students[cont])
            return msg
        cont = cont +1
    return jsonify({'Student': None})
# END METHOD DELETE

"""
books = [
    {'id': 1, 'title':'Python Fluente', 'author':'Luciano Ramalho', 'read': False},
    {'id': 2, 'title':'Pense em Python', 'author':'Luciano Ramalho', 'read': True},
    {'id': 3, 'title':'Flask Web Framework', 'author':'Luciano Ramalho', 'read': False}
]

@app.route('/api/books', methods=['GET'])
def get_books():
    return jsonify({'books': books})

@app.route('/api/books', methods=['GET', 'POST', 'PUT'])
def get_books2():
    if request.method == 'GET':
        return jsonify({'books': books})
    elif request.method == 'POST':
        return jsonify({'books': 'POST'})
    else:
        return jsonify({'books': None})

@app.errorhandler(404)
def not_found(error):
    print('error', error)
    return jsonify({'error': 'Not found...'}), 404

@app.route('/api/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    for book in books:
        if book['id'] == book_id: 
            return jsonify({'book': book['title']})
    return jsonify({"book": None})


@app.route('/')
def home():
    return 'my flask api'

@app.route('/json-example', methods=['POST'])
def json_example():
    data = request.get_json()
    title = data['title']
    author = data['author']
    return jsonify({'title': title})

# http://localhost:5000/query-example?keyword=...
@app.route('/api/books/search')
def query_example():
    keyword = request.args['keyword']
    return jsonify({'search_term': keyword})

@app.route('/api/formdata-example', methods=['POST'])
def form_data_example():
    title = request.form['title']
    category = request.form['category']
    return jsonify({'category': category})
"""