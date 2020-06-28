import json

def __read_json_file(cfg_path="options.cfg"):
    try:
        with open(cfg_path,"r") as file:
            dict = json.load(file)
        return dict
    except:
        return 0

def __write_json_file(self, cfg_path="options.cfg"): 
    try:
        with open(cfg_path,"w") as file:
            json.dump(self.stops, file)
    except:
        pass