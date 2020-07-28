from appRoute import creat_app
from appConfig.config import cfg
import redis
from flask import request
app = creat_app()



@app.before_request
def before_request():
    name = request.values.get("name")
    token = request.headers.get("token")
    return request.path
    r = redis.Redis(host='localhost', port=6379, decode_responses=True) 
    if token == r.get(name):
        print(request.headers.get("token"))
    else:
        return 'name is null'



runCif = cfg.get_config('run')
if __name__ == "__main__":
    app.run(debug= runCif['run_debug'],host= runCif['run_host'],port= runCif['run_prot'])