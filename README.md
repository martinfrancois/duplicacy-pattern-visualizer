# duplicacy-pattern-visualizer

Shows which files a set of Duplicacy include and exclude patterns lets through, as a folder tree built from a dry-run backup log.

## What it does

Duplicacy prints one `PATTERN_INCLUDE` or `PATTERN_EXCLUDE` line per path when you run a backup with `-d -enum-only`. Both scripts here read such a log, keep the paths from the `is included` lines, sort them and write them to `output.txt`. Excluded paths are dropped. Two front ends render that list as a tree:

- `duplicacy_pattern_visualizer_html.py` writes `output.txt`, which `index.html` loads and renders in the browser. Folders collapse on click. Rendering gets slow on large trees.
- `duplicacy_pattern_visualizer_ui.py` is a PyQt6 window with a file picker and a tree widget. It handles larger trees.

## Requirements

- Python 3.12 or newer. The HTML variant was tested with 3.12 and 3.13, the UI variant with 3.12 on Ubuntu 24.04.
- For the HTML variant: nothing beyond the standard library and a browser
- For the UI variant: PyQt6, pinned in `requirements.txt`, and a display

## Install

The HTML variant needs no install step.

The UI variant, on Debian or Ubuntu:

```bash
sudo apt-get install -y libglib2.0-0t64 libgl1 libegl1 libxkbcommon-x11-0 libxcb-cursor0 libxcb-icccm4 libxcb-keysyms1 libxcb-shape0 libdbus-1-3 libfontconfig1
python3 -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt
```

The UI variant, on macOS:

```bash
python3 -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt
```

The PyQt6 wheel bundles Qt itself. On Linux it still loads the X11 and OpenGL libraries of the system, which is what the `apt-get` line installs. If the import fails with `libxkbcommon.so.0: cannot open shared object file`, those libraries are missing.

## Usage

1. Run a dry-run backup with debug logging and save the output:

   ```bash
   duplicacy -log -d backup -storage <storage-name> -threads 1 -enum-only -stats > input.txt
   ```

   Replace `<storage-name>` with the name you gave the storage in `duplicacy init` or `duplicacy add`. `-enum-only` lists files without uploading anything.

2. HTML variant. Run the script in the folder that holds `input.txt` and `index.html`, then serve that folder over HTTP. Browsers refuse to `fetch()` a file next to a page opened from disk, so opening `index.html` directly shows an empty page.

   ```bash
   python3 duplicacy_pattern_visualizer_html.py
   python3 -m http.server 8000
   ```

   Open http://localhost:8000/index.html.

3. UI variant. Start the window and pick `input.txt` with the "Load File" button. The tree appears in the window and `output.txt` is written to the current directory.

   ```bash
   python3 duplicacy_pattern_visualizer_ui.py
   ```

## Example

`examples/input.txt` is an invented log with 9 included and 8 excluded paths under `data/`.

```bash
cp examples/input.txt input.txt
python3 duplicacy_pattern_visualizer_html.py
cat output.txt
```

`output.txt` lists the 9 included paths, from `data/` to `data/photos/2024/img_0003.jpg`, and none of the excluded ones such as `data/cache/` or `data/tmp/scratch.bin`. Serve the folder as described above to see the tree in the browser, or load `input.txt` in the UI variant.

## Tests

```bash
pip install -r requirements-dev.txt
python -m pytest
```

The test runs the HTML variant on `examples/input.txt` and checks the included and excluded entries. The UI variant needs a display, so CI does not run it.

## Limitations

- Both scripts read `input.txt` from and write `output.txt` to the current directory. The file names are fixed.
- Directory entries in the log end with a slash, so the HTML tree shows one empty leaf inside every folder.
- The HTML variant does not show excluded paths. To see what a pattern removed, compare `output.txt` with the `PATTERN_EXCLUDE` lines in the log.

## License

MIT, see `LICENSE`.
