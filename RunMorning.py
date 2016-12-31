# -*- coding: utf-8 -*-

import time
from slackclient import SlackClient

Token = 'token' #You must input your token key.
Chan = "#_general" #You must input your slack channel code.
Text = "모두들 새해 복 많이 받으세요~"  #Input your text.

sc = SlackClient(Token)
if sc.rtm_connect():
    while True:
        print("send")
        sc.api_call(
            "chat.postMessage",
            channel=Chan,
            text=Text
        )
