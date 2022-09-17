from flask import Flask , jsonify, request
app = Flask(__name__)

@app.route('/')
def d():
    return '시작 페이지'

@app.route('/api1', methods=['GET'])
def f1():
    return jsonify({'status': 'success'})

@app.route('/api2', methods=['POST'])
def f2():
    data = request.get_json()
    print(data)
    return jsonify(data)


app.run()