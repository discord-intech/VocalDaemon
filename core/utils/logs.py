# Outils pour l'affichage des logs

class bcolors:

    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def logGreen(text):
    print(bcolors.OKGREEN + text + bcolors.ENDC)

def logBlue(text):
    print(bcolors.OKBLUE + text + bcolors.ENDC)

def logFail(text):
    print(bcolors.FAIL + text + bcolors.ENDC)

def logHeader(text):
    print(bcolors.HEADER + text + bcolors.ENDC)

def logBold(text):
    print(bcolors.BOLD + text + bcolors.ENDC)

def logUnderline(text):
    print(bcolors.UNDERLINE + text + bcolors.ENDC)

