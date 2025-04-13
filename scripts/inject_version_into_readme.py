import json

with open("data/project-info.json", "r") as f:
    data = json.load(f)

version = data.get("version", "v0.0.0")
last_updated = data.get("last_updated", "N/A")

with open("README.md", "r") as f:
    content = f.read()

content = content.replace("<!--VERSION-->", version)
content = content.replace("<!--LAST_UPDATED-->", last_updated)

with open("README.md", "w") as f:
    f.write(content)

print("✅ Injected version into README.md")
