import fitz

pdf = "keppel-corporation-limited-annual-report-2018.pdf"

with fitz.open(pdf) as doc:
    for page in doc:
        text = page.get_text()




