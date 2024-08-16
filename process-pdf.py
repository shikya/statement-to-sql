import tkinter as tk
import fitz  # PyMuPDF
from tkinter import filedialog
import re

from constants import TOTAL, TRANSACTION, PASSWORD


# Function to open PDF and extract text with coordinates
def extract_text_with_coordinates(pdf_path, password=None):
    doc = fitz.open(pdf_path)

    # If the PDF is encrypted, try to decrypt it
    if doc.is_encrypted:
        if password:
            doc.authenticate(password)
        else:
            return None  # Return None if no password is provided

    text_elements = []

    # Iterate through pages
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        blocks = page.get_text("blocks")

        # Each block is a tuple containing:
        # (x0, y0, x1, y1, text, block_no, block_type)
        for block in blocks:
            x0, y0, x1, y1, text = block[:5]
            if text.strip():  # Ignore empty strings
                # text_elements.append((f"{x0},{y0}-{text.strip()}", x0, y0))
                text_elements.append((text.strip(), x0, y0))

    return text_elements


# Main function to create the Tkinter window and display PDF text
def main():
    pdf_path = ''

    # Extract text with coordinates
    text_elements = extract_text_with_coordinates(pdf_path, PASSWORD)
    text_elements_single = ""
    for text_element in text_elements:
        text_elements_single += text_element[0] + "\n###\n"

    # print(text_elements_single)

    # Use `re.findall` to find all matches
    matches = re.findall(TRANSACTION, text_elements_single)

    # Print all captured groups
    for match in matches:
        # `match` will be a tuple containing all the groups
        print(match)


    # Use `re.finditer` to find all matches with named groups
    matches_with_names = re.finditer(TRANSACTION, text_elements_single)

    # Print all captured named groups
    for match in matches_with_names:
        print(match.groupdict())
if __name__ == "__main__":
    main()
