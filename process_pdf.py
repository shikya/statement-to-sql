from constants import PASSWORD

from process_transactions import process_transactions
from extract_text import extract_text_with_coordinates


def main():
    """Main function to run the script"""

    pdf_path = ''

    # Extract text with coordinates
    text_elements = extract_text_with_coordinates(pdf_path, PASSWORD)
    text_elements_single = ""
    for text_element in text_elements:
        text_elements_single += text_element[0] + "\n###\n"

    pdf_data = process_transactions(text_elements_single)
    print(pdf_data)


if __name__ == "__main__":
    main()
