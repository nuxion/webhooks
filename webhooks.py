from flask import Flask, request

app = Flask(__name__)
#@app.route('/bitbucket/<repositorio>', methods = ['POST'])
@app.route('/bitbucket/<repositorio>', methods = ['POST', 'GET'])
def test(repositorio):
    if request.method=='POST': 
        resp = str(repositorio)
    else:
        resp = "invalid"
    #return 'repositorio %s addr %s \n' % resp, request.remote_addr
    #return 'add %s \n' % request.remote_addr 
    with open('request.txt', 'a') as out:
        out.write(str(request.json))
        #out.write(str(request.headers))

    return 'add %s \n' % request.headers 

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    print (post_id)
    #return 'Post %d' % post_id
if __name__ == "__main__" :
    app.run(port=5000,debug = True)
