from opsdroid.skills import match_regex
import logging
import random

import datapoint

@match_regex(r'what is the weather in (.*)\?')
async def whatistheweather(opsdroid, message):
    location = message.regex.group(1)
    api_key = opsdroid.config["skills"]["weather"]["api-key"]
    await message.respond(location + " " + api_key)
