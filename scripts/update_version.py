import json
from datetime import datetime
from pathlib import Path

info_path = Path("data/project-info.json")

# Read the file
if info_path.exists():
    with open(info_path, "r") as f:
        data = json.load(f)
else:
    data = {}

# Bump version
old_version = data.get("version", "v0.0.0")
major, minor, patch = map(int, old_version.lstrip("v").split("."))
new_version = f"v{major}.{minor}.{patch + 1}"

# Update date
today = datetime.today().strftime("%Y-%m-%d")

# Write back
data["version"] = new_version
data["last_updated"] = today

with open(info_path, "w") as f:
    json.dump(data, f, indent=2)

print(f"Updated version to {new_version} on {today}")
