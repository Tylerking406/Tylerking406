from datetime import datetime
import pytz
import re

sast = pytz.timezone("Africa/Johannesburg")
now = datetime.now(sast)
time_str = now.strftime("%I:%M %p")
date_str = now.strftime("%A, %d %B %Y")

badge_url = (
    f"![SAST Time](https://img.shields.io/badge/Cape%20Town-"
    f"{time_str.replace(' ', '%20').replace(':', '%3A')}%20SAST-378ADD?style=flat&logo=clockify&logoColor=white)"
)

block = f"<!--START_SECTION:time-->\n{badge_url}\n\n> 🗓️ {date_str} · UTC+2\n<!--END_SECTION:time-->"

with open("README.md", "r") as f:
    content = f.read()

new_content = re.sub(
    r"<!--START_SECTION:time-->.*?<!--END_SECTION:time-->",
    block,
    content,
    flags=re.DOTALL,
)

with open("README.md", "w") as f:
    f.write(new_content)

print(f"Updated time to {time_str} SAST on {date_str}")
