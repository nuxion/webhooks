import os
import sys
import subprocess
from webhooks import loghelper
import logging
from configparser import ConfigParser


def ifnotexist(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def loadConfig(section):
    """ Method wich load config file. 
    return a dict type. """
    logger = logging.getLogger(__name__)
    logger.debug("loadConfig() --> %s", section)
    parser = ConfigParser()
    # read config file
    #parser.read("config/repositories.conf") 
    # verify that in the wsgi context need the full path:
    parser.read("webhooks/config/repositories.conf")
    repository = {}
    if parser.has_section(section):
        # Return a list of tuples with the file values
        params = parser.items(section) 
        # Load all properties of the current section file
        for p in params:
            repository[p[0]]=p[1]
            #logger.debug(p)
            #print (repository) # debug
            #print (type(p)) # debug
    else:
        print ("not found, raise exception")  
    logger.debug(repository) 
    return repository


def gitExec(repository, command):
    #if not os.path.exists(repository['path']):
    #repository["path"] = "/lasdlasd"
    logger = logging.getLogger(__name__)
    logger.debug("gitExec() --> %s", repository)
    cmd = repository['gitbin'] + " -C " + repository["path"] + " " + command
    logger.debug("%s", cmd)
    logger.info("Ejecutando git en el repositorio %s", repository["path"])
    with subprocess.Popen([cmd], stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=True) as proc:
        logger.info(proc.stdout.read())
        #if proc.stderr.read():
        #    print ("fail git command")
        
        

if __name__ == "__main__":
    loghelper.setup_logging()
    #gitExec(loadConfig("souphelper"), "status")
    gitExec(loadConfig("souphelper"), "pull")
        
