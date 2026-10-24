import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPT = ROOT / "duplicacy_pattern_visualizer_html.py"
EXAMPLE = ROOT / "examples" / "input.txt"

INCLUDED = [
    "data/",
    "data/documents/",
    "data/documents/notes.txt",
    "data/documents/report.pdf",
    "data/photos/",
    "data/photos/2024/",
    "data/photos/2024/img_0001.jpg",
    "data/photos/2024/img_0002.jpg",
    "data/photos/2024/img_0003.jpg",
]

EXCLUDED = [
    "data/cache/",
    "data/cache/thumbnails.db",
    "data/documents/~$report.pdf",
    "data/photos/2024/.DS_Store",
    "data/photos/2024/raw/",
    "data/photos/2024/raw/img_0001.dng",
    "data/tmp/",
    "data/tmp/scratch.bin",
]


def test_html_variant_keeps_included_and_drops_excluded_entries(tmp_path):
    shutil.copy(EXAMPLE, tmp_path / "input.txt")

    subprocess.run([sys.executable, str(SCRIPT)], cwd=tmp_path, check=True)

    lines = (tmp_path / "output.txt").read_text().splitlines()
    assert lines == INCLUDED
    assert not set(lines) & set(EXCLUDED)
