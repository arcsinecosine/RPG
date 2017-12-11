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
            self.rand_puzzle_event = 0
            self.rand_battle_event = 0
            self.run_event = {
                1 : self.story_event_1(),
                2 : self.story_event_2(),
                3 : self.story_event_3(),
                4 : self.story_event_4(),
                5 : self.story_event_5(),
                6 : self.story_event_6()
            }

        def rand_event(self):
                self.rand_event = randint(1,6)
                self.run_event[self.rand_event]

        def story_event_1(self):



