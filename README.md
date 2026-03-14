# AI-Based Diagnostic Report Generator (DDR)

## Overview

This project processes inspection and thermal inspection reports and automatically generates a **Detailed Diagnostic Report (DDR)**.

The system extracts information from the provided PDF documents, detects potential structural issues such as dampness or leakage, and produces a structured diagnostic report summarizing the findings.

---

## Project Workflow

Inspection Report PDF  
Thermal Report PDF  

↓

Text Extraction from PDFs  

↓

Image Extraction for visual evidence  

↓

Issue Detection (dampness, cracks, leakage, moisture)

↓

DDR Report Generation

---

## Features

- Extracts **text from inspection and thermal reports**
- Extracts **images from the reports**
- Detects **common structural issues** using keyword-based analysis
- Generates a structured **Detailed Diagnostic Report**
- Provides **visual evidence references** from extracted images

---

## Project Structure
sara_shahid_shaikh
│
├── reports
│ ├── inspection_report.pdf
│ └── thermal_report.pdf
│
├── main.py
├── pdf_utils.py
├── image_utils.py
├── ddr_generator.py
├── requirements.txt
└── README.md


---

## Installation

Install dependencies:


pip install -r requirements.txt


---

## Running the Project

Run the main script:


python main.py


The program will:

1. Extract text from the reports  
2. Extract images from the reports  
3. Detect structural issues  
4. Generate a **DDR_Report.txt**

---

## Output

The system generates:

- **DDR_Report.txt** – the final diagnostic report
- **inspection_images/** – extracted inspection photos
- **thermal_images/** – extracted thermal images

---

## Example DDR Sections

- Property Issue Summary
- Area-wise Observations
- Probable Root Cause
- Severity Assessment
- Recommended Actions
- Additional Notes
- Missing Information

---

## Future Improvements

The rule-based report generation can be enhanced by integrating **Large Language Models (LLMs)** such as:

- Mistral
- Gemini
- Llama

This would enable deeper reasoning and more advanced diagnostic analysis.

---

## Author

Sara Shaikh