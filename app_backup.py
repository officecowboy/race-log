
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
