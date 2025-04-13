import json

# Load project info
with open("data/project-info.json", "r") as f:
    data = json.load(f)

version = data.get("version", "v0.0.0")
last_updated = data.get("last_updated", "N/A")

# Read README
with open("README.md", "r") as f:
    readme = f.read()

# Replace placeholders
readme = readme.replace("<!--VERSION-->", version)
readme = readme.replace("<!--LAST_UPDATED-->", last_updated)

# Write back
with open("README.md", "w") as f:
    f.write(readme)

print(f"✅ README updated to version {version}")
