import requests

url = "https://codeberg.org/zxj/xyh/raw/branch/main/live.txt"
txt = requests.get(url, timeout=30).text

out = ["#EXTM3U"]

group = "Live"

for line in txt.splitlines():
    line=line.strip()
    if not line:
        continue
    if "#genre#" in line:
        group=line.split(",")[0]
        continue
    if "," in line:
        name,link=line.split(",",1)
        out.append(f'#EXTINF:-1 group-title="{group}",{name}')
        out.append(link)

open("live.m3u","w",encoding="utf-8").write("\n".join(out))
