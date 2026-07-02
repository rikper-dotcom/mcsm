"""Test the PaperMC Fill API."""

from __future__ import annotations

import json
from pprint import pp
from urllib.request import Request, urlopen


URL = "https://fill.papermc.io/v3/projects/paper"

USER_AGENT = "mcsm-dev"


def fetch(url: str):
    """Fetch JSON from a URL."""

    request = Request(
        url,
        headers={
            "User-Agent": USER_AGENT,
        },
    )

    with urlopen(request) as response:
        return json.load(response)


def main() -> None:
    """Run the API test."""

    project = fetch(URL)

    for group, versions in project["versions"].items():
        version = versions[0]

        print(f"Checking version group: {group}")
        print(f"Using version: {version}")

        builds = fetch(
            f"{URL}/versions/{version}/builds"
        )

        stable = next(
            (
                build
                for build in builds
                if build["channel"] == "STABLE"
            ),
            None,
        )

        if stable is None:
            print("No stable build in this version.")
            print()
            continue

        print()
        print("===== STABLE BUILD FOUND =====")
        print()

        pp(stable)

        print()
        print("Downloads:")
        pp(stable["downloads"])

        print()
        print("Download keys:")
        print(stable["downloads"].keys())

        if "server:default" in stable["downloads"]:
            print()
            print("Server download:")
            pp(stable["downloads"]["server:default"])

            print()
            print("URL:")
            print(stable["downloads"]["server:default"]["url"])

        return

    print("No stable release found.")


if __name__ == "__main__":
    main()