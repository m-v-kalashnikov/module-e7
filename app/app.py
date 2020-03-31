import os

from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from flask_caching import Cache

app = Flask(__name__)

MONGO_HOST = os.environ.get('MONGO_HOST', '127.0.0.1')
REDIS_HOST = os.environ.get('REDIS_HOST', '127.0.0.1')

app.config["MONGO_URI"] = "mongodb://{}:27017/ModuleE7".format(MONGO_HOST)
app.config["CACHE_TYPE"] = "redis"
app.config["CACHE_REDIS_URL"] = "redis://{}:6379/0".format(REDIS_HOST)

mongo = PyMongo(app)
cache = Cache(app)


# Adding ad with POST method
@app.route("/ad", methods=['POST'])
def ad_poster():
    data = request.args
    if request.method == 'POST':
        if data.get('title'):
            response = mongo.db.ads.insert_one(dict(data))
            return jsonify({"massage": "Your ad id {}".format(response.inserted_id)}), 201
        else:
            return jsonify({"massage": "Your ad should contains title"}), 400


# Adding tag to existing ad with POST method
@app.route('/ad/tag/<ObjectId:ad_id>', methods=['POST'])
def tag_poster(ad_id):
    data = request.args
    if request.method == 'POST':
        if data.get('tag'):
            mongo.db.ads.update_one({"_id": ad_id}, {"$addToSet": {"tags": dict(data)}})
            return jsonify({'message': 'Tag added successfully!'}), 201
        else:
            return jsonify({'message': 'Tag is absent'}), 400


# Adding comment to existing ad with POST method
@app.route('/ad/comment/<ObjectId:ad_id>', methods=['POST'])
def comment_poster(ad_id):
    data = request.args
    if request.method == 'POST':
        if data.get('comment'):
            mongo.db.ads.update_one({"_id": ad_id}, {"$addToSet": {"comments": dict(data)}})
            return jsonify({'message': 'Comment added successfully!'}), 201
        else:
            return jsonify({'message': 'Comment is absent'}), 400


# Getting ad with GET method
@app.route('/ad/<ObjectId:ad_id>', methods=['GET'])
@cache.cached
def ad_getter(ad_id):
    if request.method == 'GET':
        response = mongo.db.ads.find_one_or_404(ad_id)
        return jsonify({'message': 'Here is your add {}'.format(response)}), 200


# Getting all ad`s with GET method
@app.route('/ads', methods=['GET'])
def ads_getter():
    if request.method == 'GET':
        try:
            response = mongo.db.ads.find()
        except TypeError:
            return jsonify({'message': 'Nothing added'}), 404
        else:
            resp = []
            for line in response:
                resp.append(line)
            return jsonify({'message': '{}'.format(resp)}), 200


# Getting statistics
@app.route('/ad/statistics/<ObjectId:ad_id>', methods=['GET'])
def statistics_getter(ad_id):
    if request.method == 'GET':
        tags = 0
        comments = 0
        response = mongo.db.ads.find_one_or_404(ad_id)
        if 'tags' in response.keys():
            for _ in response['tags']:
                tags += 1
        if 'comments' in response.keys():
            for _ in response['comments']:
                comments += 1
        return jsonify(
            {
                'message': 'Here is statistics for this ({}) ad {}'.format(ad_id, response),
                'tags': '{}'.format(tags),
                'comments': '{}'.format(comments)
            }
        ), 200


if __name__ == '__main__':
    app.run()
