import tkinter as tk
import fitz  # PyMuPDF
from tkinter import filedialog


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
    # for page_num in range(len(doc)):
    page = doc.load_page(0)
    blocks = page.get_text("blocks")

    # Each block is a tuple containing:
    # (x0, y0, x1, y1, text, block_no, block_type)
    for block in blocks:
        x0, y0, x1, y1, text = block[:5]
        if text.strip():  # Ignore empty strings
            # text_elements.append((f"{x0},{y0}-{text.strip()}", x0, y0))
            text_elements.append((text.strip(), x0, y0))

    return text_elements


# Function to draw text on the canvas
def draw_text_on_canvas(canvas, text_elements):
    for text, x, y in text_elements:
        canvas.create_text(x, y, text=text, anchor="nw", font=("Arial", 5))


# Main function to create the Tkinter window and display PDF text
def main():
    root = tk.Tk()
    root.title("PDF Text with Coordinates")

    # Define canvas size
    width = 800
    height = 1000
    canvas = tk.Canvas(root, width=width, height=height)
    canvas.pack()

    # Open a file dialog to select PDF
    pdf_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if not pdf_path:
        return

    # Extract text with coordinates
    text_elements = extract_text_with_coordinates(pdf_path, "42111415159")
    for text_element in text_elements:
        print("###")
        print(text_element[0])
    # Draw text on the canvas
    draw_text_on_canvas(canvas, text_elements)

    # canvas.create_rectangle(63, 350, 800, 800, outline="red", width=1)
    # canvas.create_rectangle(63, 60, 800, 800, outline="green", width=1)
    # Run the application
    root.mainloop()


if __name__ == "__main__":
    main()
