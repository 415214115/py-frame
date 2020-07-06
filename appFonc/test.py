from flask_restful import Resource
from flask import jsonify, request, abort, make_response, session
import time


class test(Resource):
    def get(self, name):

        session[name] = time.time()
        # session.permanent = True
        print(session.get(name))

        # tok = request.values.get('name')
        # print(session.get('name'))
        return name

class test1(Resource):
    def get(self, name):
        # session['name'] = '1111111111'
        # tok = request.values.get('name')
        if session.get(name) == None:
            return jsonify(
                msg = '登陆过期'
            )
        else:

            print(session.get(name))
            return jsonify(
                name = '熊峰',
                test = '抠脚大汉',
                tok = name
            )















        
        



        