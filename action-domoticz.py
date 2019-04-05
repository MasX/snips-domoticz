#!/usr/bin/env python3
"""This is an example of a Snips app using the Hermes protocol with the
SnipsKit library.
This app listens for an intent and answers the user.
You can find the documentation of this library in:
https://snipskit.readthedocs.io/
"""
from snipskit.hermes.apps import HermesSnipsApp
from snipskit.hermes.decorators import intent


class Domoticz(HermesSnipsApp):

    @intent('MasX:OpenShutters')
    def open_shutters(self, hermes, intent_message):
        hermes.publish_end_session(intent_message.session_id,
                                   'I received OpenShutters')

    @intent('MasX:CloseShutters')
    def close_shutters(self, hermes, intent_message):
        hermes.publish_end_session(intent_message.session_id,
                                   'I received CloseShutters')


if __name__ == "__main__":
    Domoticz()