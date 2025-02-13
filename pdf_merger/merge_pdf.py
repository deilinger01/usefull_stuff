import PyPDF2
import os

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


input_folder = r""
output_file = r""
merge_pdfs(input_folder, output_file)