from aip import AipFace

""" 你的 APPID AK SK """
APP_ID = '17826959'
API_KEY = '7mBZDyGvF9UZNeybcw3slBaT'
SECRET_KEY = 'hOhuHGcjv8K89teb2LP6beNmNWdrGpXW'

client = AipFace(APP_ID, API_KEY, SECRET_KEY)
def get_image():
    with open('1.jpg','rb') as f:
        return f.read()

import base64
image = str(base64.b64encode(get_image()),'utf8')
# print(image)

imageType = "BASE64"


""" 如果有可选参数 """
options = {}
options["face_field"] = "age,beauty,expression,gender,emotion"
options["max_face_num"] = 2
options["face_type"] = "LIVE"
options["liveness_control"] = "LOW"

""" 带参数调用人脸检测 """
res = client.detect(image, imageType, options)
print(res)

print(res.get('result').get('face_list')[0].get('age'),
    res.get('result').get('face_list')[0].get('beauty'),
    res.get('result').get('face_list')[0].get('expression').get('type'),
    res.get('result').get('face_list')[0].get('gender').get('type'),
    res.get('result').get('face_list')[0].get('emotion').get('type'))