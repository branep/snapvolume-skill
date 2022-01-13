from mycroft import MycroftSkill, intent_file_handler


class Snapvolume(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('snapvolume.intent')
    def handle_snapvolume(self, message):
        self.speak_dialog('snapvolume')


def create_skill():
    return Snapvolume()

