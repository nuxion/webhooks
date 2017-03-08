from webhooks import app 
from webhooks import gitexec 

if __name__ == '__main__': 
    app.run(debug=True) 
    #gitexec.gitExec(gitexec.loadConfig("souphelper"), "pull")

