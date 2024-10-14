import configparser

from flask import Flask

app = Flask(__name__)

def init(app):
    config = configparser.ConfigParser()
    try:
        print("INIT FUNCTION")
        config_location="etc/defaults.cfg"
        config.read(config_location)
        
        app.config['DEBUG'] = config.get("config","debug")
        app.config['ip_address'] = config.get("config","ip_address")
        app.config['port'] = config.get("config","port")
        app.config['url'] = config.get("config","url")
    except:
        print("Could not read configs from: ", config_location)
    


