# Skill pour demander au robot une info sur wikipedia

import re
import wikipedia
from core.skills.ArgSkill import ArgSkill
from core.communication import *
from core.utils.logs import *

phrases = [
    "parle moi de",
    "parles moi de",
    "que sais tu sur",
    "que sais tu de",
    "que peux tu me dire sur",
    "que peux tu me dire à propos de",
    "que peux tu dire sur",
    "qu'est-ce que tu sais sur",
    "qu'est-ce que tu sais à propos de",
    "quelle est la définition de",
    "cherche la définition sur wikipedia de",
    "cherche sur wikipedia"
]

words = [

]

badwords = [

]

def response(orderJson):

    order = orderJson["msg"]
    for phrase in phrases:
        phrase = cleanString(phrase)
        if phrase in order:
            order = re.sub(phrase, '', order)

            if orderJson["type"] == "confirmation": # Si l'ordre est déjà une confirmation :
                if isConfirmation(orderJson["answer"]): # On vérifie si la personne a dit "oui" ou "non"
                    wikipedia.set_lang("fr")
                    search = wikipedia.summary(order, sentences=1)
                    if len(search) < 40 : # Pour avoir une longueur de résultat non ridicule
                        return wikipedia.summary(order, sentences=2)
                    else:
                        return search
                else:
                    return ("Dommage ! j'en étais capable...")
            else:
                askConfirmation("Voulez vous que je recherche "+order+" sur Wikipédia ?", orderJson["msg"], orderJson["client"])
                #logBold("Response : " + "Voulez vous que je recherche "+order+" sur Wikipédia ?")
                return ""

ArgSkill(phrases, words,badwords, response)
