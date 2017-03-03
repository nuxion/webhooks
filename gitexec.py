import os
import sys
import subprocess
import loghelper 
from configparser import ConfigParser


def ifnotexist(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def loadConfig(section):
    """ Method wich load config file. 
    return a dict type. """
    
    parser = ConfigParser()
    # read config file
    parser.read("config/repositories.conf")
    repository = {}
    if parser.has_section(section):
        # Return a list of tuples with the file values
        params = parser.items(section) 
        # Load all properties of the current section file
        for p in params:
            repository[p[0]]=p[1]
            print (repository) # debug
            #print (type(p)) # debug
    else:
        print ("not found, raise exception") 
    return repository


def gitExec(repository):
    #if not os.path.exists(repository['path']):
    #repository["path"] = "/lasdlasd"
    cmd = repository['gitbin'] + " -C " + repository["path"] + " status"
    print (cmd) # debug
    with subprocess.Popen([cmd], stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=True) as proc:
        if proc.stderr.read():
            print ("fail git command")
        
        

if __name__ == "__main__":
    gitExec(loadConfig("souphelper"))
        
