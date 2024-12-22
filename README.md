# Duplicacy Include / Exclude Pattern Visualizer

## First time setup

1. ```bash
   python3 -m venv venv
   ```
2. ```bash
   source venv/bin/activate
   ```

## HTML Variant (for smaller folder trees)

1. Run a Duplicacy task with the following options: `Options: [-log -d backup -storage DropboxData -threads 1 -enum-only -stats]`
2. Save the log in this folder as `input.txt`
3. ```bash
   python3 duplicacy_pattern_visualizer_html.py
   ```
4. Run the `index.html` file  
   *(Note: it can take quite a while, depending on the size)*

## UI Variant (for larger folder trees)

### First time setup

1. ```bash
   pip3 install PyQt6
   ```
2. *(Might be necessary)*  
   ```bash
   brew install pyqt
   ```

### Instructions

1. Run a Duplicacy task with the following options: `Options: [-log -d backup -storage DropboxData -threads 1 -enum-only -stats]`
2. Save the log in this folder as `input.txt`
3. ```bash
   python3 duplicacy_pattern_visualizer_ui.py
   ```
