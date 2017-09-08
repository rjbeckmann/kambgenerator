import dice
import math
import random
import time
from kobold import skills

class Kobold():

    def __init__(self, danger_mode=False):
        
        self.brawn, self.ego, self.extranous, self.reflexes = self.roll_stats()
        self.kobold_skills = self.get_skills()

    def roll_stats(self):
        """
        Roll dice to determine base stats for kobold
        """
        stats = []
        for num in range(4):
            stats.append(dice.roll('2d6t'))
        return stats

    def handy(self, stat):
        """
        Return the handy number for a given stat
        """
        return math.ceil(stat/4)

    @property
    def hits(self):
        return self.brawn

    @property
    def meat(self):
        return self.handy(self.brawn)

    @property
    def cunning(self):
        return self.handy(self.ego)

    @property
    def luck(self):
        return self.handy(self.extraneous)

    @property
    def agility(self):
        return self.handy(self.reflexes)

    def get_skills(self, danger_mode=False):
        """
        Return a random set of skills (up to 6), the first
        four being from each distinct category, and assuming
        your kobold is actually that clever, the remaining
        two from the whole pool.
        """
        full_list = skills.brawn + skills.ego + skills.extraneous + skills.reflexes
        brawn_list = skills.brawn[:]
        ego_list = skills.ego[:]
        ref_list = skills.reflexes[:]
        list_of_lists = [brawn_list, ego_list, ref_list]

        # shuffle up
        for item in [full_list, brawn_list, ego_list, ref_list, list_of_lists]:
            random.shuffle(item)

        skill_list = []
        for num in range(self.ego):
            if num == 0:
                skill_list.append('cooking')
            elif num < 4:
                selected_list = list_of_lists.pop()
                skill_list.append(selected_list.pop())
            elif num > 6:
                break
            else:
                while True:
                    possible = full_list.pop()
                    if possible not in skill_list:
                        skill_list.append(possible)
                        break
        return skill_list
