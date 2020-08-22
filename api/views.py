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

    id_student = 0
    for student in students:
        if student['id'] - id_student > 1:
            pass
        elif id_student < student['id']:
            id_student = student['id']
    data['id'] = id_student + 1
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
