import datetime
import json

import aiohttp

from config import settings
from constants import DATE_PATERN, IAM_TOKEN_URL, SPEECH_KIT_URL
from message import ERROR_MESSAGE

IAM_TOKEN = {
    'iamToken': '',
    'expiresAt': '2022-08-02T07:23:02.093431141Z'
}


async def check_token(oauth_token):
    global IAM_TOKEN
    token_lifetime = datetime.datetime.strptime(
        IAM_TOKEN['expiresAt'][:-11], DATE_PATERN
    ) - datetime.timedelta(hours=11)
    if token_lifetime < datetime.datetime.now():
        params = {'yandexPassportOauthToken': oauth_token}
        async with aiohttp.ClientSession() as session:
            async with session.post(IAM_TOKEN_URL, params=params) as response:
                if response.status != 200:
                    return False
                content = await response.read()
                decode_response = content.decode('utf-8')
        IAM_TOKEN = json.loads(decode_response)
    return True


async def recognize(file_name):
    if await check_token(settings.oauth_token.get_secret_value()):
        headers = {'Authorization': f'Bearer {IAM_TOKEN["iamToken"]}'}
        params = {
            'lang': 'ru-RU',
            'folderId': settings.id_folder.get_secret_value(),
            'sampleRateHertz': 48000,
        }
        with open(file_name, "rb") as f:
            voice = f.read()
        async with aiohttp.ClientSession() as session:
            async with session.post(
                    SPEECH_KIT_URL,
                    params=params,
                    headers=headers,
                    data=voice
            ) as response:
                if response.status != 200:
                    return ERROR_MESSAGE
                content = await response.read()
                decode_response = content.decode('utf-8')
        text = json.loads(decode_response)["result"]
        return text
    return ERROR_MESSAGE
