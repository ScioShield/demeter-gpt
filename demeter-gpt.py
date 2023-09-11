import os
import openai
from pdfminer.high_level import extract_text
from datetime import datetime
from dotenv import load_dotenv

# Job Spec Input

def get_multiline_input():
    lines = []
    print("Enter the job description (type 'END' on a new line to finish):")
    while True:
        line = input()
        if line.strip() == "END":
            break
        lines.append(line)
    return '\n'.join(lines)

def get_generic_input():
    print("Please manually enter the job specification.")
    job_description = get_multiline_input()
    return job_description

# OpenAI API functions

def setup_api_credentials():
    load_dotenv()
    openai_key = os.getenv("OPENAI_API_KEY")
    openai.api_key = openai_key

def call_openai_api(prompt, content, model="gpt-4"):
    input_string = f"{prompt}\n{content}"
    completion = openai.ChatCompletion.create(
        model=model,
        messages=[{"role": "user", "content": input_string}]
    )
    return completion['choices'][0]['message']["content"]

# File functions

def get_filename_with_timestamp():
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    return f"application_{timestamp}.md"

def save_markdown_to_file(content, filename):
    with open(f'covers/{filename}', 'a') as file:
        file.write(content)
        file.write("\n\n")  # Separate multiple responses


def read_cv_from_pdf(pdf_path):
    return extract_text(pdf_path)

def find_cv_file():
    for filename in ["CV.pdf", "cv.pdf"]:
        if os.path.exists(filename):
            return filename
    return input("Enter the path to your CV in PDF format: ")

def synthesize_response(cv_content, job_spec, prompt):
    content = f"Job Specification:\n{job_spec}\n\nCV Details:\n{cv_content}"
    response = call_openai_api(prompt, content)
    return response

def get_user_input_question():
    print("Choose one of the following questions:")
    print("[1] Given the following job specification and my CV, please help me create a cover letter")
    print("[2] Based on the job specification and my CV what should I study for?")
    print("[3] Enter your own question.")
    
    choice = input("Enter the number corresponding to your choice: ")
    
    if choice == "1":
        return "Given the following job specification and my CV, write a cover letter"
    elif choice == "2":
        return "Based on the job specification and my CV what should I study for?"
    elif choice == "3":
        return input("Please type your question: ")
    else:
        print("Invalid choice. Please select again.")
        return get_user_input_question()
    
def sanitize_filename(filename):
    invalid_chars = ['<', '>', ':', '"', '/', '\\', '|', '?', '*']
    for char in invalid_chars:
        filename = filename.replace(char, '_')
    return filename

def get_job_details():
    company = input("What company is the job with? ").strip().replace(" ", "_").lower()  # Using underscore instead of spaces
    job_title = input("What is the job title? ").strip().replace(" ", "_").lower()  # Using underscore instead of spaces
    return company, job_title

def get_filename_with_timestamp(company, job_title):
    sanitized_company = sanitize_filename(company)
    sanitized_job_title = sanitize_filename(job_title)
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    return f"{sanitized_company}_{sanitized_job_title}_{timestamp}.md"

def main_loop():
    # Set up the API
    setup_api_credentials()

    # Fetch job details
    company, job_title = get_job_details()

    # Fetch the job spec manually
    job_spec = get_generic_input()
    if not job_spec:
        print("Failed to input job spec. Exiting.")
        exit()

    # Find the CV file
    pdf_path = find_cv_file()
    cv_content = read_cv_from_pdf(pdf_path)
    
    filename = get_filename_with_timestamp(company, job_title)
    
    while True:
        # After extracting both the CV and JD content
        prompt = get_user_input_question()
        response = synthesize_response(cv_content, job_spec, prompt)
        print(f"Response:\n{response}")

        # Save the result to a file
        save_markdown_to_file(response, filename)
        print(f"Response appended to file: covers/{filename}")

        continue_response = input("Would you like to ask another question? (yes/no): ").lower()
        if continue_response != 'yes':
            print("Bye!")
            break

if __name__ == "__main__":
    main_loop()
