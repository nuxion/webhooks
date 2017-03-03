from flask import Flask, request, jsonify, abort
import json

app = Flask(__name__)
@app.route('/git/<repositorio>', methods = ['POST'])
def getRep(repositorio):
    token = "dev"
    if validate(request, token):
        resp = str(repositorio)
    

    return 'resp: %s \n' % resp

def validate(req, token):
    if req.method=='POST': 
        compare = req.args.get('token', '')
        if compare == token:
            resp = True
        else:   
            resp = False
            abort(403)
    else:
        resp = False
    return resp
    
if __name__ == "__main__" :
    app.run(port=5000,debug = True)
