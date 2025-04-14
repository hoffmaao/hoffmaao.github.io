import os
from pathlib import Path

base = Path("content/publication")

for folder in base.iterdir():
    index_file = folder / "index.md"
    if index_file.exists():
        with open(index_file, "r") as f:
            lines = f.readlines()

        if not any("page_type:" in line for line in lines):
            for i, line in enumerate(lines):
                if line.strip() == "---" and i != 0:
                    lines.insert(i, "page_type: publication\n")
                    break

            with open(index_file, "w") as f:
                f.writelines(lines)
            print(f"✅ Updated: {index_file}")