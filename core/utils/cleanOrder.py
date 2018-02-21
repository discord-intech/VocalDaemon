# Traitement à appliquer à toutes les strings avant comparaison
# (simplifications des caractères spéciaux)

def cleanOrder(orderJson):
    order = orderJson["msg"]
    order = order.strip('?!').replace("-", " ").replace("'", " ").lstrip().rstrip().lower()
    order = order.replace("â", "a").replace("ê", "e").replace("é", "e").replace("è", "e").replace("ù", "u").replace("à", "a").replace("ô", "o")

    orderJson["msg"] = order.lstrip().rstrip()
    return orderJson

def cleanString(order):
    order = order.strip('?!').replace("-", " ").replace("'", " ").lstrip().rstrip().lower()
    order = order.replace("â", "a").replace("ê", "e").replace("é", "e").replace("è", "e").replace("ù", "u").replace("à","a").replace("ô", "o")

    return order

def cleanStringList(phrases):
    clean = []
    for i in phrases:
        clean.append(cleanString(i))
    return clean

def splitOrder(orderJson): # sépare les ordres séparés par des virgules (utile à l'écrit uniquement, google n'en met pas)
    ret = []

    orders = orderJson["msg"].split(",")
    for order in orders:
        retJson = orderJson
        retJson["msg"] = order
        ret.append(retJson)
    return ret

wordsIgnore = ["salut", "bonjour", "hey", "merci"] # Liste des mots à ignorer en cas d'ordres multiples

def toIgnore(order):
    ordWords = order.split(" ")
    for ordword in ordWords:
        if ordword in wordsIgnore:
            return True
    return False
