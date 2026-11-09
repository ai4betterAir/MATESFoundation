"""Apply approved HTML copy edits after generation and translation.

Keep these final-stage replacements separate from the layout and translation
sources. Fail if a changed source no longer contains the expected copy so a
future rebuild cannot silently discard an approved edit.
"""
import json
import re


def apply_editorial_changes(root):
    changes = json.loads((root / "editorial-changes.json").read_text())
    for relative_path, replacements in changes.items():
        path = root / relative_path
        if path.suffix != ".html" or not path.resolve().is_relative_to(root.resolve()):
            raise ValueError(f"Invalid editorial page: {relative_path}")
        content = path.read_text()
        tokens = re.split(r"(<[^>]*>)", content)
        for index, before, after in replacements:
            if index >= len(tokens) or tokens[index] not in (before, after):
                raise ValueError(f"Editorial source changed in {relative_path} at token {index}")
            tokens[index] = after
        path.write_text("".join(tokens))
