from opsdroid.matchers import match_apiai_action
import aiohttp
from urllib import parse

def weather_build_url(location):
    return "https://shlmog4lwa.execute-api.eu-west-1.amazonaws.com/dev/datapoint?location={}".format(parse.quote(location))

@match_apiai_action("weather.location")
async def weather_in_location(opsdroid, config, message):
    location = message.apiai["result"]["parameters"]["geo-city"]
    async with aiohttp.ClientSession() as session:
            async with session.get(weather_build_url(location)) as resp:
                json = await resp.json()
                await message.respond(json["properties"]["forecast"]["text"]["local"])
