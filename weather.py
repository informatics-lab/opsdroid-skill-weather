from opsdroid.skills import match_regex
import logging
import random

import datapoint

@match_regex(r'what is the weather in (.*)\?')
async def whatistheweather(opsdroid, message):
    location = message.regex.group(1)
    api_key = opsdroid.config["skills"]["weather"]["api-key"]
    conn = datapoint.connection(api_key=api_key)
    site = conn.get_nearest_site(-0.124626, 51.500728)
    forecast = conn.get_forecast_for_site(site.id, "3hourly")
    current_timestep = forecast.now()
    await message.respond("It looks like " + site.id)
