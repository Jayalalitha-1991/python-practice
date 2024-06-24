import PyPDF2
from docx import Document
import os
import re

def extract_text_from_pdf(pdf_file_path):
    with open(pdf_file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page_num in range(len(reader.pages)):
            text += reader.pages[page_num].extract_text()
        return text

def extract_text_from_docx(docx_file_path):
    doc = Document(docx_file_path)
    text = ''
    for paragraph in doc.paragraphs:
        text += paragraph.text
    return text

def extract_resume_details(text):
    patterns = {
        "Name": r'Name:\s*(.*?)\s*\n',
        "File Type": r'File\s*Type:\s*(.*?)\s*\n',
        "Resume Format": r'Resume\s*Format:\s*(.*?)\s*\n',
        "Industry": r'Industry\s*:\s*(.*?)\s*\n',
        "Location": r'Location\s*:\s*(.*?)\s*\n',
        "Job Level": r'Job\s*Level:\s*(.*?)\s*\n',
        "Years of Experience": r'Years\s*of\s*Experience:\s*(.*?)\s*\n',
        "Educational Level": r'Educational\s*Level:\s*(.*?)\s*\n',
        "Career Gap (years)": r'Career\s*Gap\s*\(\s*years\s*\):\s*(.*?)\s*\n',
        "Skills / Keywords": r'Skills\s*/\s*Keywords:\s*(.*?)\s*\n',
        "Length (pages)": r'Length\s*\(\s*pages\s*\):\s*(.*?)\s*\n',
        "Carrier Gaps": r'Carrier\s*Gaps:\s*(.*?)\s*\n'
    }

    categories = {}

    # Extracting details based on regex patterns
    for category, pattern in patterns.items():
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            categories[category] = match.group(1).strip()
        else:
            categories[category] = "N/A"  # Default value if pattern not found

    return categories

    categories = {}

    # Extracting details based on regex patterns
    for category, pattern in patterns.items():
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            categories[category] = match.group(1).strip()

    return categories


    categories = {}

    # Extracting details based on regex patterns
    for category, pattern in patterns.items():
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            categories[category] = match.group(1)

    return categories

def main():
    resume_directory = './j'
    categories = []

    for file_name in os.listdir(resume_directory):
        file_path = os.path.join(resume_directory, file_name)
        if file_name.endswith('.pdf'):
            text = extract_text_from_pdf(file_path)
        elif file_name.endswith('.docx'):
            text = extract_text_from_docx(file_path)
        else:
            continue

        resume_details = extract_resume_details(text)
        categories.append(resume_details)

    # Print extracted details for each resume
    for resume in categories:
        print("Industry Diversity:", resume.get("Industry", "N/A"))
        print("Job Level:", resume.get("Job Level", "N/A"))
        print("Years of Experience:", resume.get("Years of Experience", "N/A"))
        print("Educational Level:", resume.get("Educational Level", "N/A"))
        print("Resume Format:", resume.get("Resume Format", "N/A"))
        print("Location/Regional Variations:", resume.get("Location", "N/A"))
        print("File Type:", resume.get("File Type", "N/A"))
        print("Length:", resume.get("Length (pages)", "N/A"))
        print("Skills/Keywords:", resume.get("Skills / Keywords", "N/A"))
        print("Career Gaps:", resume.get("Career Gap (years)", "None"))
        print("\n")

if __name__ == "__main__":
    main()
