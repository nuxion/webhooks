from flask import Flask, request, jsonify
import json

app = Flask(__name__)
@app.route('/bitbucket/<repositorio>', methods = ['POST'])
def getRep(repositorio):
    
    # validate request
    if request.method=='POST': 
        resp = str(repositorio)
    else:
        resp = "invalid"
    
    #data = request.get_json()

    return 'resp: %s \n' % resp

if __name__ == "__main__" :
    app.run(port=5000,debug = True)
