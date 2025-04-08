config = {}


def setConfig(conf):
    global config
    config = conf


def getCmdp():
    if "shell" in config:
        return config["shell"]
    else:
        return "bash"


def getEditor():
    if "editor" in config:
        return config["editor"]
    else:
        return "nano"


def getProjects():
    if "projects" in config:
        return config["projects"]
    else:
        return {}
