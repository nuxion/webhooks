from flask import Flask, request, jsonify, abort
import json

app = Flask(__name__)
@app.route('/bitbucket/<repositorio>', methods = ['POST'])
def getRep(repositorio):
    token = "dev"
    # validate request
    if request.method=='POST': 
        compare = request.args.get('token', '')
        if compare == token:
            resp = str(repositorio)
        else: 
            resp = "denied"
            abort(403)
    else:
        resp = "invalid"
    
    #data = request.get_json()

    return 'resp: %s \n' % resp

if __name__ == "__main__" :
    app.run(port=5000,debug = True)
