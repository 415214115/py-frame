from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from itsdangerous import BadData
from itsdangerous import SignatureExpired
from flask import jsonify

secret_key = 'afesjyrtrw6457t'
expires_in = 7*24*60*60   # 有效期单位为秒

def get_token(id):
    # serializer = TJWSSerializer(秘钥, 有效期单位为秒)
    serializer = Serializer(secret_key, expires_in )
	
    # serializer.dumps(数据), 返回bytes类型，比如对用户的id和email进行加密返回前端
    data = {
	    'id': id,
	    'email':"415214115"
	    }
    token = serializer.dumps(data)   # data为要加密的数据
    token = token.decode()   # 得到返回后的带有效期和用户信息的加密token
    
    return token

def verify_token(token):
    # 验证失败，会抛出itsdangerous.BadData异常
    serializer = Serializer(secret_key, expires_in)

    # 2. 反序列化数据
    try:
        data = serializer.loads(token)
        # print(data)
        return data
    except Exception as e:
        return str(e)