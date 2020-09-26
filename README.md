# autotick-bot
![update-status-page](https://github.com/regro/autotick-bot/workflows/update-status-page/badge.svg) ![audit](https://github.com/regro/autotick-bot/workflows/audit/badge.svg) ![pypi-mapping](https://github.com/regro/autotick-bot/workflows/pypi-mapping/badge.svg) ![versions](https://github.com/regro/autotick-bot/workflows/versions/badge.svg) ![prs](https://github.com/regro/autotick-bot/workflows/prs/badge.svg) ![bot](https://github.com/regro/autotick-bot/workflows/bot/badge.svg) ![pacemaker](https://github.com/regro/autotick-bot/workflows/pacemaker/badge.svg)

the actual bot in an actual place doing an actual thing

# Starting and Stopping the Worker

In order to start the worker, make a commit to master with the file `please.go`
in the top-level directory.

If you want to stop the worker, simply delete this file and it will not restart
itself on the next round.

Make sure to add `ci skip` to the commit message.
