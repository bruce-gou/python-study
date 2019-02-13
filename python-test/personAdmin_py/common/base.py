
#公用模块
from django.core import serializers
import json
import base64

#返回公用方法
# res：响应对象 flg: 错误状态 布尔值  str：提示信息  data：返回的数据，status：响应状态码 默认200
def resBack(res, flg, str, data, status=200):
	if res:
		info = json.dumps({'error': flg, 'message': str, 'data': data})
		return res(info,'utf-8',status)

#转换 类对象，转成 dict 类型
def  objectTransformDict(obj):
	if isinstance(obj, object):
		data = {}
		data.update(obj.__dict__)
		del data['_state']
		return data
	else:
		return {}
#获取base64转码数据
def getBase64(data):
	info = ''
	if isinstance(data, str):
		info = base64.b64encode(bytes(data, encoding='utf-8'))
	elif isinstance(data, int) or isinstance(data, float):
		info = base64.b64encode(bytes(str(data), encoding='utf-8'))
	elif isinstance(data, dict) or isinstance(data, list):
		info = base64.b64encode(bytes(json.dumps(data), encoding='utf-8'))
	elif isinstance(data, object):
		info = base64.b64encode(bytes(json.dumps(objectTransformDict(data)), encoding='utf-8'))
	return str(info, encoding="utf-8")
# base64解码
def base64Decode(str):
    s = json.loads(base64.b64decode(str))
    return s
#操作数据库通过 .values() 方法获得值 的处理方法
def valuesFun(result):
	data = []
	for item in result:
		data.append(item)
	return data
# 获取请求头中的token中的内容
def getToken(req):
    token = req.META.get('HTTP_AUTHORIZATION').split('Bearer ')[1].split('.')[0]
    token = json.loads(base64.b64decode(token))
    return token

# 转换树形数据
def getTree(data=[],pid=0,pidName='pid',childrenName='children'):
    def fun(pid=0):
        b = []
        for x in data:
            if x[pidName] == pid:
                children = fun(x['id'])
                if len(children) > 0:
                    x[childrenName] = fun(x['id'])
                b.append(x)
        return b
    return fun(pid)

# 计算翻页取值范围
def computPage(size=10,num=1):
    y = int(size)
    x = (int(num) - 1) * y
    return [x,y]