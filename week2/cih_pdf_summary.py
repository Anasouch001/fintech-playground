import pdfplumber
import ollama
import os

# 👇 Step 1: Ask for the PDF path
pdf_path = input("📂 Enter the full path to your CIH PDF file: ").strip()

# 👇 Step 2: Extract text
def extract_text_from_pdf(pdf_path):
    try:
        text = ""
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
        return text
    except Exception as e:
        return f"⚠️ Error reading PDF: {e}"

# 👇 Step 3: Summarize using Llama3
def summarize_with_llama(text):
    if text.startswith("⚠️"):
        return text
    response = ollama.chat(
        model='llama3',
        messages=[
            {"role": "user", "content": f"Summarize this CIH bank statement:\n\n{text}"}
        ]
    )
    return response['message']['content'].strip()

# 👇 Step 4: Save summary to .txt file
def save_summary_to_file(summary_text, pdf_path):
    filename = os.path.splitext(os.path.basename(pdf_path))[0] + "_summary.txt"
    output_path = os.path.join(os.path.dirname(pdf_path), filename)
    try:
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(summary_text)
        print(f"\n✅ Summary saved to: {output_path}")
    except Exception as e:
        print(f"❌ Failed to save file: {e}")

# 👇 Step 5: Run the pipeline
if __name__ == "__main__":
    extracted_text = extract_text_from_pdf(pdf_path)
    summary = summarize_with_llama(extracted_text)
    print("\n📝 Llama3 Summary:\n")
    print(summary)
    save_summary_to_file(summary, pdf_path)
