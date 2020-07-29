
from flask_restful import Resource
from flask import jsonify, request, abort, make_response, session
import time



import redis



from appFonc.aaaaa import get_token
# app = creat_app()
class test(Resource):
    def get(self):
        # get_token(name)
        name = request.values.get("name")
        r = redis.StrictRedis(host='localhost', port=6379, db=0)
        r.set(name, get_token(name), ex=300)
        print(r.get(name).decode('ascii'))
        return jsonify(
            token = str(r.get(name).decode('ascii'))
        )











        
        



        