from flask import Flask, jsonify, request
from peewee import *
from playhouse.shortcuts import model_to_dict, dict_to_model

db = PostgresqlDatabase('races', user='sdiekema',
                        password='', host='localhost', port=5432)


class BaseModel(Model):
    class Meta:
        database = db


class Race(BaseModel):
    date = DateField(formats=['%Y-%m-%d'])
    distance = CharField()
    duration = CharField()


db.connect()
db.drop_tables([Race])
db.create_tables([Race])

Race(date='2021-09-25', distance='Half-Marathon', duration='01:20:50').save()
Race(date='2021-10-02', distance='18 Miles', duration='01:57:28').save()
Race(date='2021-11-07', distance='Marathon', duration='02:59:40').save()
Race(date='2022-03-04', distance='3000m', duration='00:09:33').save()
Race(date='2022-04-09', distance='Marathon', duration='02:44:47').save()


app = Flask(__name__)


@app.route('/race/', methods=['GET', 'POST'])
@app.route('/race/<id>', methods=['GET', 'PUT', 'DELETE'])
def endpoint(id=None):
    if request.method == 'GET':
        if id:
            return jsonify(model_to_dict(Race.get(Race.id == id)))
        else:
            peopleList = []
            for race in Race.select():
                peopleList.append(model_to_dict(race))
            return jsonify(peopleList)

    if request.method == 'PUT':
        return 'PUT request'

    if request.method == 'POST':
        new_race = dict_to_model(Race, request.get_json())
        new_race.save()
        return jsonify({"success": True})

    if request.method == 'DELETE':
        return 'DELETE request'


app.run(debug=True, port=9000)
