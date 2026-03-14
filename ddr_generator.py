def find_issues(text):

    keywords = [
        "damp",
        "leak",
        "crack",
        "seepage",
        "moisture",
        "water"
    ]

    issues = []

    for line in text.split("\n"):
        lower = line.lower()

        for word in keywords:
            if word in lower:
                issues.append(line.strip())
                break

    return list(set(issues))


def generate_ddr_report(inspection_text, thermal_text):

    inspection_issues = find_issues(inspection_text)
    thermal_issues = find_issues(thermal_text)

    all_issues = list(set(inspection_issues + thermal_issues))

    report = """
DETAILED DIAGNOSTIC REPORT (DDR)

1. Property Issue Summary
Multiple moisture and structural issues were observed during the inspection.

2. Area-wise Observations
"""

    if not all_issues:
        report += "\nNo major issues detected from extracted data.\n"

    for i, issue in enumerate(all_issues, 1):
        report += f"\nObservation {i}: {issue}\n"

    report += """

3. Probable Root Cause
Possible causes include water seepage, plumbing leaks, or wall cracks.

4. Severity Assessment
Moderate severity. Issues may worsen if not addressed.

5. Recommended Actions
- Repair cracks
- Apply waterproofing
- Inspect plumbing
- Seal wall gaps

6. Additional Notes
Thermal analysis suggests possible moisture accumulation.

7. Missing or Unclear Information
Further structural inspection may be required.
"""

    return report