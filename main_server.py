# Vocal interface
import socket
import json
from core.utils.logs import *
from core.utils.cleanOrder import *
from core import core
from core.communication import *

sockRobot=socket.socket()
# sockRobot.connect(("127.0.0.1", 56987))
# sockRobot.send(str.encode("motordaemon"))

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind(('', 15555))



logHeader("######################")
logHeader("#    VOCAL SERVER    #")
logHeader("######################")

while(42):

    logUnderline("--- Attente de requete ---")

    socket.listen(5)
    client, address = socket.accept()

    logGreen("Client connecte...\n")

    try :
        orderJson = recvFromClient(client)

        if (orderJson["type"] == "question" or orderJson["type"] == "confirmation"):
            #print("Reçu ordre de type " + orderJson["type"])
            #print("Request : ")
            #logBlue(orderJson["msg"])

            orderJson["client"] = client
            orderJson = cleanOrder(orderJson)

            ret = core.executeSkill(orderJson)  # TODO tout transformer en JSON !!!

            if (ret != ""):
                #logBold("Response : " + ret)
                sendAnswer(ret, client)

            print("Close")
            client.close()
        else:
            print("ORDRE DE TYPE NON RECONNU : " + str(orderJson))
            ret = "ERREUR : Le message envoye au serveur n'est pas un bon Json"
            logFail("Response : " + ret)
            sendError(ret, client)
            print("Close")
            client.close()


    except KeyError:
        ret = "ERREUR : Le message envoye au serveur n'est pas un bon Json"
        logFail("Response : " + ret)
        sendError(ret, client)
        print("Close")
        client.close()
    #except ValueError :
    #    ret = "ERREUR : Le message envoye au serveur n'est pas un Json"
    #    logFail("Response : " + ret)
    #    sendError(ret, client)
    #    print("Close")
    #    client.close()



    print("\n--------------\n")
