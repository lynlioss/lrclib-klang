"""Package the versioned manifest for a GitHub release. No Android build is needed."""
import hashlib
import json
import re
from pathlib import Path

source = Path("plugin.json").read_bytes()
plugin = json.loads(source)
assert plugin["apiVersion"] == 1
assert re.fullmatch(r"(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)", plugin["version"])
assert plugin["repository"] == "https://github.com/lynlioss/lrclib-klang"
assert plugin["type"] == "lyrics" and 1 <= len(plugin["lyrics"]["requests"]) <= 4
Path("plugin.json.sha256").write_text(hashlib.sha256(source).hexdigest() + "  plugin.json\n")
