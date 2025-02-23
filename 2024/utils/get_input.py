import requests
import os
from dotenv import load_dotenv

load_dotenv()


def get_input(year, day, test=False):
    if test:
        f = open("test_input.txt", "r")
        data = f.read()
        return data
    headers = {'Cookie': f'session={os.getenv("session")}'}
    url = f'https://adventofcode.com/{year}/day/{day}/input'
    r = requests.get(url=url, headers=headers)
    return r.text