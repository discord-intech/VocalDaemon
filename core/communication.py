import json
from core.utils.cleanOrder import cleanString

yesWords = ["oui", "d'accord", "d accord", "ok", "ça marche", "pourquoi pas", "bien sur"]
noWords = ["non", "pas du tout", "hors de question", "pas question", "impossible", "je refuse"]

def sendAnswer(answer, client):
    msg = { "type": "answer", "msg": answer }
    jsonMsg = json.dumps(msg)
    client.send(str.encode(jsonMsg))

def sendError(answer, client):
    msg = { "type": "ERROR", "msg": answer }
    jsonMsg = json.dumps(msg)
    client.send(str.encode(jsonMsg))


def askConfirmation(confirmMessage, originalRequest, client):
    msg = {"type": "askConfirmation", "msg": confirmMessage, "originalRequest": originalRequest}
    jsonMsg = json.dumps(msg)
    client.send(str.encode(jsonMsg))

def isConfirmation(str):
    for word in noWords:
        if word in cleanString(str):
            return False
    for word in yesWords:
        if word in cleanString(str):
            return True
    return False

def recvFromClient(client):
    rawOrder = client.recv(1024).decode('utf-8')
    #print(rawOrder)

    orderJson = json.loads(rawOrder)

    if(orderJson == "") :
        raise ValueError("Json Vide")

    return orderJson
