import re

# Define the regex pattern for matching lines that contain "is included"
pattern = re.compile(r'.*is included.*')

# Define the regex pattern for extracting the relevant part of the matching lines
extract_pattern = re.compile(r'PATTERN_INCLUDE\s+(.+?)\s+is included')

# Read the input file and filter lines
with open('input.txt', 'r') as file:
    lines = file.readlines()

# Store the extracted parts in a list
extracted_lines = []

for line in lines:
    if pattern.match(line):
        match = extract_pattern.search(line)
        if match:
            extracted_lines.append(match.group(1))

# Sort the extracted lines alphabetically
extracted_lines.sort()

# Write the sorted lines to the output file
with open('output.txt', 'w') as file:
    for extracted_line in extracted_lines:
        file.write(extracted_line + '\n')
