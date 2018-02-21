# coding=utf-8
# Core of Hermes-vocal

from core.skills import skillsLoader
from core.utils.cleanOrder import *



def executeSkill(orderJson):  # Traitement d'un ordre (complexe)

    order = orderJson["msg"]
    if(order == "") :
        return "Je ne vous ai pas entendu"
    orders = order.split(",")  # On regarde si on peut séparer l'ordre en 2 (si il y a une virgule)
    returns = []
    if len(orders) > 1: # Ordre multiple
        for order in orders:
            if not toIgnore(order):
                newOrderJson = orderJson
                newOrderJson["msg"] = order.lstrip().rstrip()
                returns.append(computeOrder(newOrderJson) + "\n") # On ne répond qu'aux ordres pertinents
        finalreturn = ""
        for a in returns:
            finalreturn += a
        return finalreturn
    else:
        return computeOrder(orderJson)


def computeOrder(orderJson):    # Traitement d'un ordre simple (splité)
    for skill in skillsLoader.SkillsList:
        if skill.ask(orderJson["msg"]):  # Si la phrase demandée est connue
            return skill.execute(orderJson)

    scores = []  # Sinon, on calcule les scores de similarité
    for skill in skillsLoader.SkillsList:
        scores.append(skill.similitude(orderJson["msg"]))

    maxSimilitude = max(scores)
    maxSimilitudeIndex = scores.index(maxSimilitude)

    secScores = []
    secScores += scores
    secScores[maxSimilitudeIndex] = 0

    secMaxSimilitude = max(secScores)
    secMaxSimilitudeIndex = scores.index(secMaxSimilitude)

    print(scores) # Debug

    if (secMaxSimilitude == maxSimilitude):
        print("2 phrases de meme similarite !")
        return "Je ne comprends pas cette phrase."

    if (maxSimilitude == 0):  # Si on a aucun mot commun nulle part
        print("Pas de mot commun !")
        return "Je ne comprends pas cette phrase."

    if maxSimilitude > 3 * secMaxSimilitude:
        if (maxSimilitude >= 10):
            return (skillsLoader.SkillsList[maxSimilitudeIndex].execute(orderJson))


    return ("Je ne comprends pas cette phrase")
