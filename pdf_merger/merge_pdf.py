import PyPDF2
import os
import fitz

def merge_pdfs(input_folder, output_file):
    if os.path.exists(input_folder) == True:
        pdf_merger = PyPDF2.PdfMerger()

        # get a list of all PDF files in the input folder
        pdf_files = [file for file in os.listdir(input_folder) if file.endswith(".pdf")]
        pdf_files.sort()
        # merge each PDF file into the merger object
        for pdf_file in pdf_files:
            file_path = os.path.join(input_folder, pdf_file)
            pdf_merger.append(file_path)

        # write the merged PDF to the output file
        with open(output_file, "wb") as output:
            pdf_merger.write(output)
        print('Merged the PDFs.')
    else:
        print('Input path doesnt exist.')

def merge_pdfs_fitz(input_folder, output_file):
    doc = fitz.open()
    pdf_files = sorted([file for file in os.listdir(input_folder) if file.endswith(".pdf")])

    for pdf_file in pdf_files:
        file_path = os.path.join(input_folder, pdf_file)
        doc.insert_pdf(fitz.open(file_path))

    doc.save(output_file)
    print("Merged the PDFs using pymupdf.")

input_folder = r""
output_file = r""
merge_pdfs(input_folder, output_file)
