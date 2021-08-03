from flask import Blueprint, jsonify, request

main = Blueprint('main', __name__)

@main.route('/get_results', methods=["GET"])
def get_results():
    # TODO run model

    res = [
        {"URL":"dad", "Source":"sdsd","Date" :"", "IsLatest":True, "IsLessThanFifty" :True},
        {"URL":"fsafsaf", "Source" :"sdsd","Date":"","IsLatest":False,"IsLessThanFifty" :False}]
    return jsonify(res)

@main.route('/', methods=["GET"])
def home():
    return "Hello"

@main.route('/post_features', methods=["POST"])
def post_features():
    feature_set = request.get_json()
    print(f"feature set type -> {type(feature_set)}, \n feature_set -> {feature_set}")
    return 'Features received', 201