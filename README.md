# PDF Splitter
---
`pdf_splitter` is a Python application that splits PDF files into multiple smaller PDFs, each with a specified number of pages. By default, it splits PDFs into 50-page sections.

## Features

- Splits the first PDF file found in the `input/` folder.
- Saves the split PDF files in the `output/` folder with the same base name, followed by a sequential number.
- By default, each split PDF contains 50 pages, but this number is configurable.

## Requirements

- Python 3.6 or higher.
- The `PyPDF2` library for PDF manipulation.

Install dependencies by running the following command:

```bash
pip install -r requirements.txt
```

## Folder Structure
The project follows this folder structure:

```
pdf_splitter/
├── input/
│   └── <file.pdf>
├── output/
│   └── <file_split_1.pdf>
│   └── <file_split_2.pdf>
├── pdf_splitter.py
└── requirements.txt
```

## Usage
1. Place the PDF file you want to split into the input/ folder.
2. Run the pdf_splitter.py script in the project’s root directory:

```bash
python pdf_splitter.py
```

3. The split files will be created in the output/ folder, named <original_name_1>.pdf, <original_name_2>.pdf, etc.


## Configuration
To change the number of pages per split, adjust the `pages_per_split` variable in the `split_pdf` function. For example, to split with 20 pages per PDF:

```
pages_per_split = 20
```

## Notes

- Ensure the `input/` and `output/` folders exist in the project’s root directory before running the script.
- The script only processes the first PDF file found in the `input/` folder.

## License

This project is licensed under the MIT License.
