def __read_cfg_file(cfg_path="options.cfg"):
    import json
    try:
        with open(cfg_path,"r") as file:
            dict = json.load(file)
        return dict
    except:
        return 0