#!/usr/bin/env python3
"""This is an example of a Snips app using the Hermes protocol with the
SnipsKit library.
This app listens for an intent and answers the user.
You can find the documentation of this library in:
https://snipskit.readthedocs.io/
"""
from snipskit.hermes.apps import HermesSnipsApp
from snipskit.hermes.decorators import intent
from snipskit.config import AppConfig
import requests


class Domoticz(HermesSnipsApp):

    @intent('MasX:OpenShutters')
    def open_shutters(self, hermes, intent_message):
        if self.set_shutter_level(1):
            hermes.publish_end_session(intent_message.session_id,
                                        'Shutters opened.')
        else:
            hermes.publish_end_session(intent_message.session_id,
                                       'Encountered an issue opening the shutters.')

    @intent('MasX:CloseShutters')
    def close_shutters(self, hermes, intent_message):
        if self.set_shutter_level(99):
            hermes.publish_end_session(intent_message.session_id,
                                       'Shutters closed.')
        else:
            hermes.publish_end_session(intent_message.session_id,
                                       'Encountered an issue closing the shutters.')

    def set_shutter_level(self, level):
        hostname = self.config['secret']['hostname']
        switch_no = self.config['secret']['switch_no']
        r = requests.get("{}/json.htm?type=command&param=switchlight&idx={}&switchcmd=Set%20Level&level={}"
                         .format(hostname, switch_no, level), verify=False)
        return r.status_code == 200


if __name__ == "__main__":
    Domoticz(config=AppConfig())
