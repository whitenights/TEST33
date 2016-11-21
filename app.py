from flask import Flask
from flask import request
from flask import render_template
import json

app = Flask(__name__)


@app.route('/')
def index():
    if request.args:
        eng = request.args['eng']
        f = open('eng-thai.json','r',encoding='utf-8-sig')
        engthai = json.loads(f.read())
        if eng in engthai:
            return ', '.join(engthai[eng])
        else:
            return 'No such word in a dictionary'
    return render_template("index.html")

if __name__ == '__main__':
    app.run()
