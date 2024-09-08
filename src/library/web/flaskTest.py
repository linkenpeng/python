'''
pip install flask
Flask: web应用开发微框架

Jemeter: avarage:101ms TPS: 900 

stop: 
lsof -i :5000 | awk 'NR>1 {print $2}' |xargs kill -9
'''

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    data = 'Hello, Flask!'
    response = {"code":200, "message":"success", "data":data}
    return response

if __name__ == '__main__':
    app.run()
