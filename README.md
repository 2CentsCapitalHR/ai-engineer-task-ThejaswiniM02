[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/vgbm4cZ0)

#  ADGM Document Compliance Checker

This tool checks corporate documents against ADGM (Abu Dhabi Global Market) legal requirements using a Retrieval-Augmented Generation (RAG) approach.  
It identifies missing or non-compliant items and provides direct citations from ADGM laws.

## Features
- Document Type Detection (Articles of Association, Service Agreement, Privacy Policy)
- Checklist Compliance Check for each document type
- RAG-powered Law Retrieval from ADGM sources
- Outputs:
  - Annotated DOCX with comments for each issue
  - JSON report of all findings

## Setup

1. **Clone this repository**
   git clone https://github.com/2CentsCapitalHR/ai-engineer-task-ThejaswiniM02.git
   cd ai-engineer-task-ThejaswiniM02
   
Create & activate virtual environment:
python -m venv venv
# Windows
venv\Scripts\activate

Install dependencies:
pip install -r requirements.txt

Add your API key:
- Create a .env file in the project root:
- GEMINI_API_KEY=your_google_generative_ai_api_key

Build RAG vectorstore:
-python rag_setup.py

Run the App:
streamlit run app.py

- Upload a .docx file
- View missing compliance items and related laws
- Download annotated DOCX and JSON report

Included Test Documents:
- aoa_good.docx — Fully compliant Articles of Association
- service_partial.docx — Partially compliant Service Agreement
- privacy_partial.docx — Partially compliant Privacy Policy
- compliance_disaster.docx — Multiple issues for testing

Notes
The vector store adgm_vectorstore/ is already built from official ADGM sources.
For best results, use clear, well-structured .docx documents.

Author
Thejaswini M
AI Engineer Task Submission – 2Cents Capital
