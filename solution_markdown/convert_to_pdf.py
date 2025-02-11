import markdown
from fpdf import FPDF

with open("appel_offres.md", "r", encoding="utf-8") as f:
    html = markdown.markdown(f.read())

pdf = FPDF()
pdf.add_page()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.set_font("Arial", size=12)
pdf.multi_cell(0, 10, html)
pdf.output("appel_offres.pdf")
