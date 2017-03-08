# Generls imports
from flask import Flask, request, jsonify, abort 
import logging
# Project specify imports
from webhooks import app
from webhooks import gitexec 
from webhooks import loghelper


""" Startup application. """
#app = Flask(__name__, instance_relative_config=True)
# load config from instance/
#app.config.from_pyfile('config.py') 

# start routes
@app.route('/git/<repositorio>', methods = ['POST'])
def getRep(repositorio):
    """ Recieve and exec the actualization of the repo. """ 
    logger= logging.getLogger(__name__)
    if validate(request):
        resp = str(repositorio)
        logger.info("repositorio --> %s", resp)
        gitexec.gitExec(gitexec.loadConfig(resp), "status")
    

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
    loghelper.setup_logging()
    app.run(port=5000,debug = True)
