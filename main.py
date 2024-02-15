'''
Created By Rana Jay on 15-02-2024
'''

from flask import Flask, jsonify, request

app = Flask(__name__)

cars = [
    {"id":1 , "carname":"car1", "owner":"jay"},
    {"id":2 , "carname":"car2", "owner":"rahul"},
    {"id":3 , "carname":"car3", "owner":"dhruv"}
]

@app.route('/cars', methods=['GET'])
def get_cars():
    return jsonify({'cars': cars})

# reading data 
@app.route('/cars/<int:car_id>', methods=['GET'])
def get_car(car_id):
    for car in cars:
        if car['id'] == car_id:
            return car
    return {'error': 'car not found'}

# adding car
@app.route('/cars', methods=['POST'])
def add_car():
    car = {'id': len(cars) + 1, 'carname': request.json['carname'], 'owner': request.json['owner']}
    cars.append(car)
    return car

# upadating data
@app.route('/cars/<int:car_id>', methods=['PUT'])
def update_car(car_id):
    for car in cars:
        if car['id'] == car_id:
            car['carname'] = request.json['carname']
            car['owner'] = request.json['owner']
            return car
    return {'error': 'car not found'}

# deleting car
@app.route('/cars/<int:car_id>', methods=['DELETE'])
def delete_car(car_id):
    for car in cars:
        if car['id'] == car_id:
            cars.remove(car)
            return {'message': 'car deleted'}
    return {'error': 'car not found'}

if __name__ == '__main__':
    app.run(debug=True)