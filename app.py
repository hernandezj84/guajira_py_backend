"""Flask server that provides json document for the light-sensor project"""

import json
from flask import Flask, jsonify, request, make_response
from flask_cors import CORS
from database import Database

app = Flask(__name__)
app.config["JSON_SOR_KEYS"] = False
app.config["CORS_HEADERS"] = 'Content-Type'
cors = CORS(app, resources={r"/*": {"origins": "*"}})

OK_STATUS = 200
NOT_FOUND_STATUS = 404
DATABASE = database = Database()

@app.route("/test/")
def test():
    """Returns a hard-coded message indication that the application is running properly

    Returns:
        make_response: simple json message indicating that everithing is working fine
    """
    response_data = {"message": "everything is ok"}
    return make_response(jsonify(response_data))

@app.route("/post_lecture/", methods=(['POST', ]))
def post_lecture():
    """Post a change on light sensor

    Returns:
        make_response: json string that informs is the insertion was successful
    """
    status = OK_STATUS
    posted_data = request.json
    response = DATABASE.insert_light_sensor(posted_data["device"], posted_data["information"])
    response_data = {"status": OK_STATUS, "mktime": response}
    return make_response(jsonify(response_data), status)

@app.route("/get_device/<device_name>/", methods=(['GET', ]))
def get_device_info(device_name):
    """Gets all the registries of the 'device_name

    Args:
        device_name (str): device name registries to be found

    Returns:
        make_response: json string with all the registries from device
    """
    status = NOT_FOUND_STATUS
    response_data = {"status": status, "error": "No device found"}
    data = DATABASE.get_light_sensor(device_name)
    if data:
        status = OK_STATUS
        response_data = data
    return make_response(jsonify(response_data), status)
