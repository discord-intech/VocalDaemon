from core.skills.Skill import Skill
import psutil

# Utilisation CPU :

phrases = [
    "donne moi ton utilisation CPU",
    "donne moi ton utilisation processeur",
    "à quel niveau est ton processeur",
    "à quel niveau est ton CPU",
    "quel est le niveau d'utilisation de ton processeur",
    "quel est le niveau d'utilisation de ton cpu",
    "comment va ton processeur",
    "comment va ton cpu",
    "à quel pourcentage est ton processeur",
    "à quel pourcentage est ton cpu",
    "quel est l'état de ton processeur",
    "quel est l'état de ton cpu"
]

words = [
    "processeur",
    "cpu"
]

badwords = [

]

def result():
    return ("Mon processeur est à "+str(psutil.cpu_percent())+" pourcents de ses capacités.")

Skill(phrases, words, badwords, result)

# Etat de la RAM

phrases = [
    "donne moi ton utilisation RAM",
    "donne moi ton utilisation de mémoire RAM",
    "donne moi ton utilisation de mémoire vive",
    "à quel niveau est ta RAM",
    "à quel niveau est ta mémoire RAM",
    "à quel niveau est ta mémoire vive",
    "quel est le niveau d'utilisation de ta RAM",
    "quel est le niveau d'utilisation de ta mémoire RAM",
    "quel est le niveau de ta mémoire vive",
    "comment va ta RAM",
    "comment va ta mémoire RAM",
    "comment va ta mémoire vive",
    "à quel pourcentage est ta RAM",
    "à quel pourcentage est ta mémoire RAM",
    "à quel pourcentage est ta mémoire vive",
    "quel est l'état de ta RAM",
    "quel est l'état de ta mémoire RAM",
    "quel est l'état de ta mémoire vive"
]

words = [
    "RAM",
    "mémoire RAM",
    "mémoire vive"
]

badwords = [

]

def result():
    return ("J'utilise actuellement "+str(int((psutil.virtual_memory().available/psutil.virtual_memory().total)*100))+" pourcents de ma mémoire RAM.")

Skill(phrases, words, badwords,result)