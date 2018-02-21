import random
from core.skills.skillsLoader import SkillsList
from core.utils.cleanOrder import *


class Skill:
    def __init__(self, keyphrases, superwords,badwords, result):
        self.keyphrases = cleanStringList(keyphrases)  # On clean les phrases connues et les mots clés
        self.superwords = cleanStringList(superwords)
        self.badwords = cleanStringList(badwords)
        miscKeyPhrases = [wordPhrase.split() for wordPhrase in self.keyphrases]
        miscKeyWords = []
        for miscKeyphrase in miscKeyPhrases:
            miscKeyWords += miscKeyphrase

        self.keywords = []
        for keyword in miscKeyWords:
            if keyword not in self.keywords:
                self.keywords.append(keyword)  # Séparation en mots clés uniques

        #print("Skill loaded : " + self.keyphrases[0])
        self.result = result
        SkillsList.append(self)

    def ask(self, order):
        # Verification 1 : Phrase exacte
        for i in self.keyphrases:
            if (cleanString(i) == order):
                return True
        return False

    def similitude(self, order):
        # Vérification 2 : Proximité avec l'ordre
        orderWords = order.split()
        res = 0
        for orderWord in orderWords:
            ##print("Modele : " + orderWord)
            for keyword in self.keywords:
                ##print("test : "+keyword)
                if keyword == orderWord:    # Chaque mot commun ajoute 1 point (doublons non comptés)
                    ##print("MATCH !!!")
                    res += 1
        for superkeyword in self.superwords:
            if superkeyword in order:   # Chaque superword présent ajoute un bonus de 10
                res += 20
        for badkeyword in self.badwords:
            if badkeyword in order:   # Chaque superword présent ajoute un bonus de 10
                res -= 20

        return res

    def execute(self,
                *args):  # On laisse *args car on fournit toujours orders pour les skills hérités qui en ont besoin
        return (self.result())


from core.skills.ArgSkill import *  # Ajoute le support des skills avec argument
