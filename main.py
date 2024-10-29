import PyPDF2
import os
from typing import Optional


def split_pdf(pages: int) -> Optional[None]:
    """
    Splits the first PDF found in the 'input/' directory into multiple smaller PDFs with the specified number of pages per split.

    Args:
        pages (int): The number of pages each split PDF should contain.

    Returns:
        None if successful, otherwise prints an error if no PDF is found in the input directory.
    """
    # Define input and output directory paths
    input_dir = "input"
    output_dir = "output"

    # Check if input directory exists, create it if not
    if not os.path.exists(input_dir):
        os.makedirs(input_dir)  # Create the input directory

    # Check if output directory exists, create it if not
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)  # Create the output directory

    # Find the first PDF file in the input dir
    pdf_files = [f for f in os.listdir(input_dir) if f.endswith(".pdf")]
    if not pdf_files:
        print("No PDF files found in the input dir.")
        return

    # Get full path of the first PDF file found and its base name (without extension)
    input_pdf_path = os.path.join(input_dir, pdf_files[0])
    pdf_name = os.path.splitext(pdf_files[0])[0]

    # Open the input PDF file
    with open(input_pdf_path, "rb") as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        total_pages = len(pdf_reader.pages)

        # Create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)

        # Split the PDF into smaller parts
        for i in range(0, total_pages, pages):
            pdf_writer = PyPDF2.PdfWriter()
            # Add pages to the current split
            for j in range(i, min(i + pages, total_pages)):
                pdf_writer.add_page(pdf_reader.pages[j])

            # Define output path with sequence number
            output_pdf_path = os.path.join(output_dir, f"{pdf_name}_{i // pages + 1}.pdf")
            # Write the split PDF to the output directory
            with open(output_pdf_path, "wb") as output_pdf_file:
                pdf_writer.write(output_pdf_file)

    print("PDF split successfully.")


# Modify with the desired number of pages per split
pages_per_split = 6

split_pdf(pages_per_split)
