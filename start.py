from appRoute import creat_app
from appConfig.config import cfg
import redis
from flask import request
from appFonc.aaaaa import verify_token

app = creat_app()



@app.before_request
def before_request():
    if request.path != '/test':
        name = request.values.get("name")
        token = request.headers.get("token")
        r = redis.Redis(host='localhost', port=6379, decode_responses=True)
        redisToken = r.get(name)
        if redisToken:
            # return str(redisToken)
            if token != str(redisToken):
                return 'token不正确'
            else:
                r.setex(name, 30, token)
                return verify_token(token)
        else:
            return verify_token(token)



runCif = cfg.get_config('run')
if __name__ == "__main__":
    app.run(debug= runCif['run_debug'],host= runCif['run_host'],port= runCif['run_prot'])