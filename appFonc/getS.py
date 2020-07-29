from flask_restful import Resource
from flask import jsonify, request, abort, make_response, session
from appFonc.aaaaa import verify_token
import jwt
import redis
class test1(Resource):
    def get(self):
        # session['name'] = '1111111111'
        token = request.headers.get("token")
        name = request.values.get("name")
        # print(verify_token(token))
        # verify_token(token)
        # r = redis.StrictRedis(host='localhost', port=6379, db=0)
        # if r.get(name):
        #     r.setex(name, 30, token)
            # time.sleep(30)
        # return str(r.get(name).decode('ascii'))
        # return  verify_token(token)
        return '000'




        # if session.get(name) == None:
        #     return jsonify(
        #         msg = 'no session'
        #     )
        # else:
        #     print(session.get(name))
        #     return jsonify(
        #         msg = 'is session',
        #         value = session.get(name)
        #     )















        
        



        