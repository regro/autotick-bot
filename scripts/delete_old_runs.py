import github
import os
import sys
import requests
import datetime
import time
import typer

app = typer.Typer()


@app.command()
def main(token: str = "", max_runs: int = 200):
    token = token or os.environ.get("GITHUB_TOKEN", "")
    if not token:
        raise RuntimeError("Requires GITHUB_TOKEN env var to be set")

    gh = github.Github(token)
    r = gh.get_repo("regro/autotick-bot")
    done = 0
    for w in r.get_workflows():
        for _ in range(10):
            for rn in w.get_runs():
                if rn.status == "completed" and (
                    datetime.datetime.utcnow() - rn.updated_at
                    > datetime.timedelta(days=365)
                ):
                    requests.delete(
                        rn.url,
                        headers={
                            "Authorization": "Bearer " + os.environ["GITHUB_TOKEN"]
                        },
                    )
                    done += 1
                    time.sleep(2)
                if done >= max_runs:
                    return


if __name__ == "__main__":
    app()
