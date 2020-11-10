if 'please.go' in @(ls):
    mv please.go please.stop
    git add please.stop
    s = 'stop in the name of bot'
else:
    mv please.stop
    git add please.go
    s = 'let it go, let it gooooo'
git commit -am @(f"[CI SKIP] {s}")
git push
