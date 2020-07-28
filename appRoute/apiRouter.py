from flask_restful import Api
from flask import jsonify
# from ApiRoute.router import test
import appRoute.router
api = Api()

apiList = appRoute.router

api.add_resource(apiList.test,'/test')
api.add_resource(apiList.test1,'/test1')


# api.add_resource(apiList.image,'/image')