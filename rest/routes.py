import json
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from process.links_process import LinksProcess


app = Flask(__name__)
cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"


@app.route("/link/readall", methods=["GET"])
@cross_origin()
def read_all():

    process = LinksProcess()
    result = process.get_all_links()

    if not result:
        return "Ocurred an error when trying to read links", 400

    return jsonify(result), 200


@app.route("/link/save", methods=["POST"])
@cross_origin()
def save():
    parameters = request.args.to_dict()

    url = parameters.get("url")
    label = parameters.get("label")

    if not all([url, label]):
        return "No parameters to save.", 400

    process = LinksProcess()
    result = process.create_link(url=url, label=label)

    if not result:
        return "Ocurred an error when trying to create links", 400

    return "Success", 200


@app.route("/link/edit", methods=["POST"])
@cross_origin()
def edit():
    parameters = request.args.to_dict()

    link_id = parameters.get("id")
    url = parameters.get("url")
    label = parameters.get("label")

    if not link_id:
        return "No id in the request.", 400

    if not any([url, label]):
        return "Any data to edit.", 400

    process = LinksProcess()
    result = process.edit_link(link_id=link_id, url=url, label=label)

    if not result:
        return "Ocurred an error when trying to edit links", 400

    return "Success.", 200


@app.route("/link/delete", methods=["POST"])
@cross_origin()
def delete():
    parameters = request.args.to_dict()
    link_id = parameters.get("id")

    if not link_id:
        return "No id in the request.", 400

    process = LinksProcess()
    result = process.delete_link(link_id=link_id)

    if not result:
        return "Ocurred an error when trying to delete links", 400

    return "Success.", 200
