import json
from datetime import datetime

# Paths
info_path = "data/project-info.json"
readme_path = "README.md"

# Load project info
with open(info_path, "r") as f:
    data = json.load(f)

version = data.get("version", "v0.0.0")
last_updated = data.get("last_updated", str(datetime.today().date()))

# Load README
with open(readme_path, "r") as f:
    readme = f.read()

# Replace placeholders
readme = readme.replace("<!--VERSION-->", version)
readme = readme.replace("<!--LAST_UPDATED-->", last_updated)

# Save updated README
with open(readme_path, "w") as f:
    f.write(readme)

print("✅ Injected version and last updated into README.md")
