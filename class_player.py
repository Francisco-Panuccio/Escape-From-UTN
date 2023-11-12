import os
import json
from variables import *

class Player:
    def __init__(self, name, language, score) -> None:
        self.name = name
        self.language = language
        self.score = score

    def write_file(path_file, write_file):
        with open(path_file, "w", encoding="utf-8") as file:
            json.dump(write_file, file, indent=4)

    def read_and_load_file(path_file):
        retorno = None
        if (os.path.exists(path_file)):
            if (os.stat(path_file).st_size == 0):
                retorno = False
            else:
                with open(path_file, "r", encoding="utf-8") as file:
                    load_list = json.load(file)
                    retorno = load_list
        else:
            retorno = False
        return retorno


    def save_player_config(config_file, language):
        config = {"Config": []}
        config["Config"].append({"Language": language})
        Player.write_file(config_file, config)

    def load_player_config(config_file):
        return Player.read_and_load_file(config_file)


    def save_player_data(score_file, name, score):
        min = {"value": None}
        data_player = (Player.load_player_data(score_file))
        if ((data_player == False) or (data_player == None)):
            data["Players"].append({"Name": name, "Score": str(score)})
            Player.write_file(score_file, data)
        else:
            if (len(data_player["Players"]) > 2):
                for i in range(len(data_player["Players"])):
                    if (min["value"] == None or int(data_player["Players"][i]["Score"]) < int(score)):
                        min["value"] = int(data_player["Players"][i]["Score"])
                for i in range(len(data_player["Players"])):
                    if (int(data_player["Players"][i]["Score"]) == min["value"]):
                        data_player["Players"][i]["Name"] = name
                        data_player["Players"][i]["Score"] = str(score)
                    break
            else:
                data_player["Players"].append({"Name": name, "Score": str(score)})
            Player.write_file(score_file, data_player)

    def load_player_data(score_file):
        return Player.read_and_load_file(score_file)