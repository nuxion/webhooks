from flask import Flask, request, jsonify
import json

app = Flask(__name__)
#@app.route('/bitbucket/<repositorio>', methods = ['POST'])
@app.route('/bitbucket/<repositorio>', methods = ['POST', 'GET'])
def test(repositorio):
    if request.method=='POST': 
        resp = str(repositorio)
    else:
        resp = "invalid"
    #return 'repositorio %s addr %s \n' % resp, request.remote_addr
    data = request.get_json()
    tipo = type(data[0])
    with open('request.log', 'a') as out:
        #out.write(str(request.json))
        out.write(str(tipo))

    #return 'add %s \n' % request.headers 
    #return jsonify(json.loads(request.data))
    #return jsonify(request.json)
    #print (data[0])    
    return str(data[0])
    #return jsonify(data)
    #return 'user: %s \n' % user

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    print (post_id)
    #return 'Post %d' % post_id
if __name__ == "__main__" :
    app.run(port=5000,debug = True)
