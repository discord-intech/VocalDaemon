# Fonctions d'appel au robot
# A transformer lors de l'intégration !

from core.utils.logs import *

def goto(position):
    logGreen("LE ROBOT VA VERS : "+position)

def forward():
    logGreen("LE ROBOT AVANCE")
