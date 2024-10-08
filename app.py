
import os
from flask import Flask, jsonify, request
app=Flask(__name__)
from routes import register_routes

@app.route('/',methods=['GET'])
def get_hello():
    return "hello"

register_routes(app)






# app.run(debug=True)
if __name__ =='__main__':
    port=int(os.environ.get('PORT',5006))
    app.run(debug=False, host='0.0.0.0',port=port)