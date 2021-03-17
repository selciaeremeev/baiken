# coding: utf-8
import os
import datetime
import requests
from bs4 import BeautifulSoup

DAT = datetime.date.today().strftime("%Y_%m_%d")
FILENAME = f"{os.path.splitext(os.path.basename(__file__))[0]}_{DAT}.txt"


def output(url: str, tag: str, start: int) -> None:
    soup = BeautifulSoup(requests.get(url).text, "html.parser")
    with open(FILENAME, "a") as f:
        for line in soup.find(tag).get_text().split("\n")[start:]:
            f.write(f"{line}\n")


output("https://free-proxy-list.net/", "textarea", 3)
