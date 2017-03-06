from flask import Flask, request, jsonify, abort
import json


""" Startup application. """
app = Flask(__name__, instance_relative_config=True)
# load config from instance/
app.config.from_pyfile('config.py') 

# start routes
@app.route('/git/<repositorio>', methods = ['POST'])
def getRep(repositorio):
    if validate(request):
        resp = str(repositorio)
    

    return 'resp: %s \n' % resp

def validate(req):
    """ Validate if the token is ok. """
    if req.method=='POST': 
        compare = req.args.get('token', '')
        if compare == app.config['SECRET_KEY'] :
            resp = True
        else:   
            resp = False
            abort(403)
    else:
        resp = False
    return resp
    
if __name__ == "__main__" :
    app.run(port=5000,debug = True)
