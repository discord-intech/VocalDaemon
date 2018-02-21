from core.skills.Skill import *
from core.skills.skillsLoader import SkillsList
import json

class TextSkill(Skill):

    def result(self):
        return (random.choice(self.results))

    def __init__(self, keyphrases, superwords,badwords, results):

        self.results = results
        super().__init__(keyphrases, superwords,badwords, self.result)



# Chargement des TextSkills depuis le json

with open('core/skills/phrases.json', encoding='utf-8') as data_file:
    data = json.load(data_file)

for skill in data["skillList"] :
    TextSkill(skill["keyPhrases"], skill["superWords"], skill ["badWords"],skill["responses"])