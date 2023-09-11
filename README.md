# Demeter-GPT
This Python script is designed to assist in customizing your job applications to specific job descriptions, through the use of OpenAI's GPT-4 LLM.  
Note the output is not going to be perfect and the LLM can and does make mistakes so poof read and edit all outputs.  

## Features
Submit a custom job description from Indeed, LinkedIn, etc. and your CV to OpenAI and get a response back.  
There are three default prompts:  
1. Given the following job specification and my CV, please help me create a cover letter  
2. Based on the job specification and my CV what should I study for?  
3. Enter your own question.  

All prompts synthesize the Job Description and CV so contextual questions can be asked and answered, like the above. Option 3 allows for free text input, example "What tech stacks would the company benefit from, that I can bring to this position?", "What are excellent interview questions based on my CV and the Job Description?", etc.  

## Requirements
### OpenAI
You will need your own OpenAI API key (that can access the GPT-4 model)  
Create a .env file that looks like .env.example with your API key  

### Python 3  
- openai
- pdfminer
- dotenv

All requirements can be installed with  
`python3 -m pip install -r requirements.txt --user`

### A CV
Place a CV in PDF format in this directory with the name `CV.pdf` or `cv.pdf`

## Usage
To use the script simply place your OpenAI API key in the `.env` file. Once running you will be promoted to input the job description, just paste it into the terminal window, then you will see a list of questions, ask away, and it'll be saved in the covers directory.  

## TO DO
- Add `.docx` support  
- Add a local LLM flag?  
- Cost estimates like in the Sibyl scripts?
- GUI?
- ~~Job title section? (could make more meaningful filenames)~~

## Attempted
In the initial stages of the script I attempted pulling the JDs directly from job sites, this wasn't viable as some sites respond with a `403` and others don't have a section to pinpoint the description.  

## Demo
With the [Awesome CV](https://github.com/posquit0/Awesome-CV) as input and a "Junior Infra (Linux) Engineer" job description from LinkedIn these are the results:  

```
$ python3 demeter-gpt.py
What company is the job with? Hunter Bond
What is the job title? Junior Infra (Linux) Engineer
Please manually enter the job specification.
Enter the job description (type 'END' on a new line to finish):
About the job
[REMOVED]
END
Choose one of the following questions:
[1] Given the following job specification and my CV, please help me create a cover letter
[2] Based on the job specification and my CV what should I study for?
[3] Enter your own question.
Enter the number corresponding to your choice: 1
Response:
Dear Hiring Manager,

I am writing to express my interest in the Junior Infra (Linux) Engineer position that was posted on Sep 11, 2023. My twelve years of software engineering experience have furnished me with a comprehensive skill set that aligns with the job specifications you listed. 

In my current role as Site Reliability Engineer and Infrastructure Team Lead at KarrotPay, a fintech company, I have led significant growth in the infrastructure departments. Included among my accomplishments is the design and provisioning of the entire infrastructure on the AWS cloud, thereby enabling KarrotPay to meet necessary security compliance and procure a business license for providing financial services in Korea. I have also implemented continuous improvements to the infrastructure architecture since the launch of the service which now caters to 3.6 million users

Major projects have included migrating the orchestration system from DC/OS to Kubernetes and managing complex network configurations on AWS. I also provided an observability system with Kafka, Elastic Stack and implemented utilisation of configuration management tools such as Terraform. 

Additionally, my development and deployment of several API microservices using Node.js, Koa and AWS Lambda functions are testaments to my scripting and automation capabilities. I also have a strong grounding in monitoring tools like Grafana, InfluxDB, ELK, and Prometheus, having deployed centralized logging and monitoring environments.

Although I have not had formal financial experience, the fintech companies I have worked for have provided me with invaluable knowledge of securing and optimizing critical infrastructures while also adhering to financial regulations.

Counter to your 'nice to have' prerequisites, I have substantial experience in operating within multi-threading, distributed systems and I'm confident that my knowledge on low latency experience will be an asset considering the high-performing operations within your trading environment.

I am captivated by the operation of trading firms particularly one like yours that employs sophisticated scientific methods to maximize investment returns. Being part of a highly progressive team is an opportunity I relish and the chance to contribute my skills to one of the leading quantitative firms in the country, is an exciting prospect.

Thank you for considering my application. I look forward to the opportunity to discuss how my skills and experiences will be of benefit to your team.

Yours sincerely,

Byungjin Park

Response appended to file: covers/hunter_bond_junior_infra_(linux)_engineer_20230911162318.md
Would you like to ask another question? (yes/no): no
```