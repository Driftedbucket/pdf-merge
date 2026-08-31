from pathlib import Path

from pypdf import PdfWriter

base_dir = Path(__file__).parent

output_pdf = base_dir / "campus_market_final_v1.pdf"

pdf_files = [
    base_dir / "CampusMarket-v2.pdf",
    base_dir / "campus_market_cost_estimate.pdf",
    base_dir / "campus_market_financials.pdf"
]

writer = PdfWriter()

for pdf in pdf_files:
    if not pdf.exists():
        raise FileNotFoundError(f"Missing input PDF: {pdf}")
    writer.append(str(pdf))

with open(output_pdf, "wb") as f:
    writer.write(f)

writer.close()

print(f"Merged {len(pdf_files)} PDFs into {output_pdf} ({len(writer.pages)} pages)")
