import json
from datetime import datetime

file_path = "data/project-info.json"

try:
    with open(file_path, "r") as f:
        data = json.load(f)
except FileNotFoundError:
    print(f"❌ ERROR: Could not find {file_path}")
    exit(1)
except json.JSONDecodeError as e:
    print(f"❌ JSON error: {e}")
    exit(1)

version = data.get("version", "v0.0.0").lstrip("v")
major, minor, patch = map(int, version.split("."))
patch += 1
new_version = f"v{major}.{minor}.{patch}"

data["version"] = new_version
data["last_updated"] = datetime.today().strftime("%Y-%m-%d")

with open(file_path, "w") as f:
    json.dump(data, f, indent=2)

print(f"✅ Updated version to {new_version}")

