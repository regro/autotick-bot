import os
import sys
import tempfile
import subprocess
import contextlib
import json
import time


# https://stackoverflow.com/questions/6194499/pushd-through-os-system
@contextlib.contextmanager
def pushd(new_dir):
    previous_dir = os.getcwd()
    os.chdir(new_dir)
    try:
        yield
    finally:
        os.chdir(previous_dir)


heartbeat_file = sys.argv[1] + ".json"

with tempfile.TemporaryDirectory() as tmpdir, pushd(tmpdir):
    subprocess.run(
        ["git", "clone", "https://github.com/regro/autotick-bot.git"],
        check=True,
    )
    with pushd("autotick-bot"):
        subprocess.run("git checkout heartbeats", check=True, shell=True)

        heartbeat = int(time.time())
        with open(heartbeat_file, "w") as fp:
            json.dump({"heartbeat": heartbeat}, fp)

        subprocess.run(
            ["git", "add", heartbeat_file],
            check=True,
        )

        subprocess.run(
            "git commit --allow-empty -am '[ci skip] heartbeat %s'" % sys.argv[1],
            check=True,
            shell=True,
        )

        subprocess.run(
            "git remote set-url --push origin "
            "https://${PASSWORD}@github.com/regro/autotick-bot.git",
            shell=True,
            check=True,
        )

        i = 0
        pushed = False
        while not pushed and i < 10:
            try:
                subprocess.run(
                    "git push",
                    check=True,
                    shell=True,
                )
                pushed = True
            except subprocess.CalledProcessError:
                subprocess.run("git pull --rebase", shell=True)
            i += 1

    if not pushed:
        sys.exit(1)
