# Duplicacy Include / Exclude Pattern Visualizer

## First time setup

1. ```bash
   python3 -m venv venv
   ```
2. ```bash
   source venv/bin/activate
   ```

## HTML Variant (for smaller folder trees)

1. Run a Duplicacy task with the following options: `Options: [-log -d backup -storage <storage-name> -threads 1 -enum-only -stats]`\
   *(Replace `<storage-name>` with the name of your storage)*
2. Save the log in this folder as `input.txt`
3. ```bash
   python3 duplicacy_pattern_visualizer_html.py
   ```
4. Serve this folder over HTTP\
   *(Browsers don't let a page opened from disk load `output.txt`, so opening `index.html` directly shows an empty page)*
   ```bash
   python3 -m http.server 8000
   ```
5. Open <http://localhost:8000/index.html>\
   *(Note: it can take quite a while, depending on the size)*

## UI Variant (for larger folder trees)

### First time setup

1. ```bash
   pip3 install -r requirements.txt
   ```
2. If needed on macOS:
   ```bash
   brew install pyqt
   ```

On Linux, the Qt UI also requires native GLib libraries. If importing PyQt6 fails
with `ImportError: libgthread-2.0.so.0: cannot open shared object file`, install the
package that provides that library using your distribution's package manager.
For example, openSUSE provides it in `libgthread-2_0-0`; other distributions use
different package names. Pip installs the Python dependencies but does not install
this system library. The HTML processing script does not need Qt or GLib.

Check the UI dependencies without opening a window:

```bash
QT_QPA_PLATFORM=offscreen python3 -c 'from PyQt6.QtWidgets import QApplication; app = QApplication([])'
```

This checks Qt initialization only. Native file dialogs and desktop integration
still need a graphical session.

### Instructions

1. Run a Duplicacy task with the following options: `Options: [-log -d backup -storage <storage-name> -threads 1 -enum-only -stats]`\
   *(Replace `<storage-name>` with the name of your storage)*
2. Save the log as a `.txt` file
3. ```bash
   python3 duplicacy_pattern_visualizer_ui.py
   ```
4. Click "Load File" and select the log\
   *(The tree appears in the window and `output.txt` is written to the current folder)*
