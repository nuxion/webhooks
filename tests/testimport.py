import logging
import loghelper
import gitexec

loghelper.setup_logging()
logger= logging.getLogger(__name__)

gitexec.gitExec(gitexec.loadConfig("souphelper"), "status")
