import json
from pathlib import Path

info_path = Path("data/project-info.json")
readme_path = Path("README.md")

# Load version info
with open(info_path, "r") as f:
    data = json.load(f)

version = data.get("version", "v0.0.0")
last_updated = data.get("last_updated", "unknown")

# Load README
with open(readme_path, "r") as f:
    content = f.read()

# Replace placeholders
content = content.replace("<!--VERSION-->", version)
content = content.replace("<!--LAST_UPDATED-->", last_updated)

# Save back
with open(readme_path, "w") as f:
    f.write(content)

print("✅ Injected version and last updated into README.md")
