# Skill pour demander au robot de nous guider

import core.robot as robot
from core.skills.ArgSkill import ArgSkill
from core.communication import *

with open('core/map.json', encoding='utf-8') as data_file:
    map = json.load(data_file)

phrases = [
    "guide moi",
    "amène moi",
    "amene moi",
    "emmene moi",
    "ou est",
    "je veux aller",
    "je dois aller",
    "j'aimerai aller",
    "je voudrais aller",
    "va à",
    "va au"
]

words = [
    "guide",
    "amene",
    "emmene"
]

badwords = [

]

def response(orderJson):
    order = orderJson["msg"]
    for l in map["label"]:
        if cleanString(l["text"]) in order:
            if orderJson["type"]=="confirmation":
                if isConfirmation(orderJson["answer"]):
                    robot.goto(l["text"])
                    return("Je vous amène à "+l["text"])
                else:
                    return "Dommage, j'aime bien me ballader"
            else:
                askConfirmation("Voulez vous que je vous amène à "+l["text"]+" ?", orderJson["msg"], orderJson["client"])
                return ""
    return("Je n'ai pas compris votre destination.")

ArgSkill(phrases, words,badwords, response)



phrases2 = ["Avance", "Avance d'un mètre", "Avance un peu"]

words2 = ["avance"]
badwords2 = []

def response2(orderJson):
    robot.forward()
    return("Chaud devant !")

ArgSkill(phrases2, words2, badwords2, response2)
