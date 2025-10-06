from pypdf import PdfReader, PdfWriter

# List your PDFs in the desired order
pdf_files = [
    "AZ-900.pdf",
    "PL-900.pdf",
    "MB-920.pdf",
    "DotNetWithCSharp.pdf"
]

writer = PdfWriter()

for pdf in pdf_files:
    reader = PdfReader(pdf)
    for page in reader.pages:
        writer.add_page(page)

# Output combined PDF
with open("Microsoft_Certificates_Combined.pdf", "wb") as f:
    writer.write(f)

print("Merged PDF created: Microsoft_Certificates_Combined.pdf")
