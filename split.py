import os
from PyPDF2 import PdfReader, PdfWriter

def split_pdf(input_pdf_path: str, output_folder: str):
    """
    Split a multi-page PDF into separate single-page PDF files.

    Parameters:
    - input_pdf_path: str, path to the input PDF file.
    - output_folder: str, folder path where the split PDFs will be saved.
    """
    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Open the PDF file
    pdf = PdfReader(input_pdf_path)
    total_pages = len(pdf.pages)
    base_name = os.path.splitext(os.path.basename(input_pdf_path))[0]

    # Iterate over each page and save it as a new PDF
    for page_num in range(total_pages):
        pdf_writer = PdfWriter()
        pdf_writer.add_page(pdf.pages[page_num])

        output_filename = os.path.join(output_folder, f"{base_name}_page_{page_num + 1}.pdf")
        with open(output_filename, 'wb') as output_file:
            pdf_writer.write(output_file)

        print(f"Created: {output_filename}")

# Example usage
if __name__ == "__main__":
    input_pdf = "example.pdf"           # Path to your input PDF
    output_dir = "split_pages_output"  # Output directory for split PDFs
    split_pdf(input_pdf, output_dir)
