#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def generate_report(pdf_location, title, description):
    styles = getSampleStyleSheet()
    report = SimpleDocTemplate(pdf_location)

    report_title       = Paragraph(title, styles["h1"])
    report_description = Paragraph(description)

    report.build([report_title, report_description])