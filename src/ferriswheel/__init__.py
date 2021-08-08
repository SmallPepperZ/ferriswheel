import aiohttp
import asyncio
import guilds
import messages
import channels
import users

api_uri = "https://api.ferris.chat/api/v0/"

GET /guilds/{guild_id}
GET /users/{user_id}
GET /channels/{channel_id}
GET /channels/{channel_id}/message/{message_id}

async def run_client(token: str):
    auth_headers = {"Authorization": token}
    async with aiohttp.ClientSession(headers=auth_headers) as session:
        async with session.get(api_uri) as response:
            
            print("Status:", response.status)
            html = await response.text()
            print("Body:", html[:15], "...")
        return session


def run(token: str):
    loop = asyncio.get_event_loop()
    session = loop.run_until_complete(run_client(token))
    async def get_guild(guild_id: int):
        async with session.get(api_uri + "guilds/" + str(gulld_id)) as response:
            class Data:
                status = response.status
                
