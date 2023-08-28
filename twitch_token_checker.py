from typing import TextIO

import aiohttp
import asyncio
import time
import logging

from aiohttp import ClientSession

logging.getLogger().setLevel(logging.INFO)

URL = "https://id.twitch.tv/oauth2/validate"
CURRENT_DATE_FORMAT = "%H.%M.%S %m-%d-%Y"


async def check_token(session: ClientSession, token: str, file: TextIO) -> str:
    headers = {"Authorization": f"OAuth {token}"}
    async with session.get(URL, headers=headers) as response:
        if response.status == 200:
            file.write(f"{token}\n")
            logging.info(f"{token} is valid")
            return token

        elif response.status == 401:
            logging.warning(f"{token} is not valid")

        elif response.status == 429:
            return await check_token(session, token, file)


async def check_tokens(input_file_name: str) -> (int, int):
    with open(input_file_name, "r", encoding="utf-8", errors="ignore") as file:
        tokens = file.read().splitlines()

    current_date = time.strftime(CURRENT_DATE_FORMAT)
    output_file_name = f"{current_date}.txt"

    async with aiohttp.ClientSession() as session:
        with open(output_file_name, "a+", encoding="utf-8", errors="ignore") as file:
            tasks = [check_token(session, token, file) for token in tokens]
            results = await asyncio.gather(*tasks)

    valid_tokens = [token for token in results if token is not None]

    return len(tokens), len(valid_tokens)


async def main() -> None:
    while True:
        input_file = input("Enter the path to the file with the Twitch tokens: ")
        start_time = time.time()
        count_tokens, count_valid_tokens = await check_tokens(input_file)
        end_time = time.time()
        logging.info(f"Valid Tokens: {count_valid_tokens}/{count_tokens}\n"
                     f"Checking {count_tokens} tokens took {end_time - start_time} seconds")


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main())