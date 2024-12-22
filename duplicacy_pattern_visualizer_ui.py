import re
import os
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTreeWidget, QTreeWidgetItem, QVBoxLayout, QWidget, QPushButton, QFileDialog, QMessageBox

# Function to read and filter the lines from the input.txt file and write to output.txt
def process_input_file(input_path, output_path):
    pattern = re.compile(r'.*is included.*')
    extract_pattern = re.compile(r'PATTERN_INCLUDE\s+(.+?)\s+is included')

    with open(input_path, 'r') as file:
        lines = file.readlines()

    extracted_lines = []
    for line in lines:
        if pattern.match(line):
            match = extract_pattern.search(line)
            if match:
                extracted_lines.append(match.group(1))

    extracted_lines.sort()

    with open(output_path, 'w') as file:
        for line in extracted_lines:
            file.write(line + '\n')

    return extracted_lines

# Function to create a tree structure from the file paths
def create_tree(paths):
    root = {}
    for path in paths:
        parts = path.split('/')
        current = root
        for part in parts:
            if part not in current:
                current[part] = {}
            current = current[part]
    return root

# Function to insert the tree structure into the tree view
def insert_tree(tree, parent_item):
    for key, value in tree.items():
        if key:  # Skip any empty keys
            item = QTreeWidgetItem([key])
            parent_item.addChild(item)
            if value:
                insert_tree(value, item)

class FileExplorer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("File Explorer")
        self.setGeometry(300, 300, 600, 400)

        self.tree_widget = QTreeWidget()
        self.tree_widget.setHeaderLabels(["File Structure"])

        self.load_button = QPushButton("Load File")
        self.load_button.clicked.connect(self.load_file)

        layout = QVBoxLayout()
        layout.addWidget(self.load_button)
        layout.addWidget(self.tree_widget)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def load_file(self):
        input_path, _ = QFileDialog.getOpenFileName(self, "Select input.txt", "", "Text Files (*.txt)")
        if input_path:
            try:
                output_path = 'output.txt'
                file_paths = process_input_file(input_path, output_path)
                tree = create_tree(file_paths)

                self.tree_widget.clear()
                insert_tree(tree, self.tree_widget.invisibleRootItem())

                QMessageBox.information(self, "Success", "Processed input.txt and created output.txt")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to load file: {e}")

# Main function to run the application
def main():
    app = QApplication(sys.argv)
    window = FileExplorer()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
