from random import randint
class world:
    class dungeon_kfc:
        def __init__(self):
            self.events = {
                story_event_1 : False,
                story_event_2 : False,
                story_event_3 : False,
                puzzle_event_1 : False,
                puzzle_event_2 : False,
                puzzle_event_3 : False,
                battle_event_1 : False,
                battle_event_2 : False,
                battle_event_3 : False
                    }
            self.rand_event = 0
            
        def rand_event(self):
            while True:
                self.rand_event = randint(1,3)
                if (self.rand_event == 1):
                    if (self.events[story_event_1] == False):
                        self.story_event_1()
                    elif (self.events[story_event_2] == False):
                        self.story_event_2()
                    elif (self.events[story_event_3] == False):
                        self.story_event_3()
                    else:
                        return ("All story events done")
