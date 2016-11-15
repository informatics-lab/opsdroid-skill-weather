from opsdroid.skills import match_regex
import logging
import random

import datapoint

def getforecast(opsdroid, location):
    api_key = opsdroid.config["skills"]["weather"]["api-key"]
    conn = datapoint.connection(api_key=api_key)
    site = conn.get_nearest_site(-0.124626, 51.500728)
    return conn.get_forecast_for_site(site.id, "3hourly")

@match_regex(r'what is the weather in (.*)\?')
async def whatistheweather(opsdroid, message):
    location = message.regex.group(1)
    forecast = getforecast(opsdroid, location)

    await message.respond("It looks like it is {} in {}".format(
                              forecast.days[0].timesteps[0].weather.text +
                              ,location))
