# SplitPDF

A simple Python utility to split multi-page PDF files into individual single-page PDFs using the `PyPDF2` library.

## Description

SplitPDF allows you to easily split a PDF document into separate pages, saving each page as an individual PDF file. This is useful for extracting specific pages or breaking down large PDFs into smaller, manageable files.

## Features

- Split multi-page PDFs into single-page PDF files
- Easy-to-use Python interface
- Supports all PDF files supported by PyPDF2
- Minimal dependencies

## Installation

Install PyPDF2 via pip:

```
pip install PyPDF2
```

Clone the repository:

```
git clone https://github.com/enrique-web/SplitPDF.git
cd SplitPDF
```

## Usage

Example Python code to split a PDF into individual pages:

```
from PyPDF2 import PdfReader, PdfWriter
import os

def split_pdf(input_pdf_path: str, output_folder: str):
    os.makedirs(output_folder, exist_ok=True)
    reader = PdfReader(input_pdf_path)
    total_pages = len(reader.pages)
    base_name = os.path.splitext(os.path.basename(input_pdf_path))

    for page_num in range(total_pages):
        writer = PdfWriter()
        writer.add_page(reader.pages[page_num])

        output_path = os.path.join(output_folder, f"{base_name}_page_{page_num + 1}.pdf")
        with open(output_path, "wb") as output_pdf:
            writer.write(output_pdf)
        print(f"Created: {output_path}")

if __name__ == "__main__":
    input_pdf = "example.pdf"           # Replace with your PDF file path
    output_dir = "split_pages_output"  # Folder to save split pages
    split_pdf(input_pdf, output_dir)
```

## Notes

- The output files are named using the original filename plus the page number.
- The output folder will be created if it does not exist.
- Works with PDFs of any length.

## Contributing

Contributions, bug reports, and feature requests are welcome! Please open issues or submit pull requests.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
```
