from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
import mycroft.audio
from mycroft.util.log import LOG

class DemoSkill(MycroftSkill):
    SEC_PER_LETTER = 0.65
    LETTERS_PER_SCREEN = 9.0

    def __init__(self):
        super(DemoSkill, self).__init__(name="DEMOSKILL")

    @intent_handler(IntentBuilder("DemoIntent").require("query").require("Demo"))
    def handle_query_demo(self, message):
        # set the ultimate song
        ultimate_song = "'More Than a Feeling' by Boston"
        self.enclosure.deactivate_mouth_events() 
        self.enclosure.mouth_text(ultimate_song)
        self.speak_dialog("The ultimate song is ", ultimate_song)
        time.sleep((self.LETTERS_PER_SCREEN + len(ultimate_song)) * self.SEC_PER_LETTER)

        mycroft.audio.wait_while_speaking()
        self.enclosure.activate_mouth_events()
        self.enclosure.mouth_reset()

def create_skill():
    return DemoSkill()
