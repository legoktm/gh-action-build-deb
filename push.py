#!/usr/bin/env python3
import subprocess
import sys
from pathlib import Path

SUPPORTED = {
    "debian": [
        "buster",
        "bullseye",
        "bookworm",
        "trixie",
        "unstable"
    ],
    "ubuntu": [
        "bionic",
        "eoan",
        "focal",
        "groovy",
        "hirsute",
        "impish",
        "jammy",
        "kinetic",
        "lunar",
        "mantic",
        "noble",
    ]
}

# TODO: autogenerate README.md listing

def main():
    dockerfile = Path("Dockerfile").read_text()

    all_branches = subprocess.check_output(["git", "branch"], text=True)
    for distro, versions in SUPPORTED.items():
        for version in versions:
            branch = f"{distro}-{version}"
            image = f"{distro}:{version}"
            if branch in all_branches:
                subprocess.check_call(["git", "branch", "-D", branch])

            subprocess.check_call(["git", "checkout", "-b", branch, "main"])
            Path("Dockerfile").write_text(
                dockerfile.replace("{{FROM}}", image))
            subprocess.check_call(["git", "add", "Dockerfile"])
            subprocess.check_call(["git", "commit", "-m", branch])
            if "--push" in sys.argv:
                subprocess.check_call(["git", "push", "origin", branch, "-f"])


if  __name__ == "__main__":
    main()
