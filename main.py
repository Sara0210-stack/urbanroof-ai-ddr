from pdf_utils import extract_text
from image_utils import extract_images
from ddr_generator import generate_ddr_report

inspection_path = r"C:\Sara_Shahid_Shaikh\.venv\reports\Inspection_report.pdf"
thermal_path = r"C:\Sara_Shahid_Shaikh\.venv\reports\Thermal_report.pdf"

print("Extracting text...")

inspection_text = extract_text(inspection_path)
thermal_text = extract_text(thermal_path)

print("Extracting images...")

extract_images(inspection_path, "inspection_images")
extract_images(thermal_path, "thermal_images")

print("Generating Detailed Diagnostic Report (DDR)...")

report = generate_ddr_report(inspection_text, thermal_text)

with open("DDR_Report.txt", "w") as f:
    f.write(report)

print("DDR Report generated successfully!")