import fitz  # PyMuPDF

def extract_text_with_coordinates(pdf_path, password=None):
    """Function to open PDF and extract text with coordinates"""

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
