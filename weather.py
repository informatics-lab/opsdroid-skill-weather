from opsdroid.matchers import match_regex, match_apiai_action
import logging
import random
import aiohttp

import datapoint

def getforecast(config, location):
    api_key = config["api-key"]
    conn = datapoint.connection(api_key=api_key)
    site = conn.get_nearest_site(-0.124626, 51.500728)
    return conn.get_forecast_for_site(site.id, "3hourly")

def weather_build_url(location):
    return "https://shlmog4lwa.execute-api.eu-west-1.amazonaws.com/dev/datapoint?location=Milton%20Keynes"

@match_regex(r'what is the weather in (.*)\?')
async def whatistheweather(opsdroid, config, message):
    location = message.regex.group(1)
    forecast = getforecast(config, location)

    await message.respond("It looks like it is {} in {}".format(
                              forecast.days[0].timesteps[0].weather.text,
                              location))

@match_apiai_action("weather.location")
async def weather_in_location(opsdroid, config, message):
    location = message.apiai["result"]["parameters"]["geo-city"]
    logging.debug(location)
    async with aiohttp.ClientSession() as session:
            async with session.get(weather_build_url(location)) as resp:
                json = await resp.json()
                await message.respond(json["properties"]["forecast"]["text"]["regional"])
