import json
import datetime
import os

info_path = "data/project-info.json"

# Load existing version info
with open(info_path, "r") as f:
    data = json.load(f)

# Increment patch version
version = data["version"].lstrip("v").split(".")
version[-1] = str(int(version[-1]) + 1)
new_version = "v" + ".".join(version)

# Update the version and date
data["version"] = new_version
data["last_updated"] = str(datetime.date.today())

# Save it back
with open(info_path, "w") as f:
    json.dump(data, f, indent=2)

print(f"✅ Updated version to {new_version}")
