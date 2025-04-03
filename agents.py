import os
import smtplib
import groq
from dotenv import load_dotenv
from crewai import Agent
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from updating_CRM import update_google_sheet


load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
SENDER_EMAIL = "aadityaxalt73@gmail.com"
SENDER_PASSWORD = "lhhd mmjr eozl pvno" 

client = groq.Client(api_key=GROQ_API_KEY)


lead_generator = Agent(
    role="Lead Generator",
    goal="Identify potential leads from form responses.",
    backstory="An AI agent specialized in filtering interested customers based on their form submissions.",
    verbose=True
)

engagement_agent = Agent(
    role="Engagement Agent",
    goal="Generate personalized emails based on user expectations.",
    backstory="A marketing AI assistant responsible for crafting engaging emails to build customer relationships.",
    verbose=True
)

sales_agent = Agent(
    role="Sales Agent",
    goal="Classify leads and decide on the next action.",
    backstory="An experienced sales strategist who categorizes leads into Hot, Warm, or Cold and plans follow-ups.",
    verbose=True
)

# Function to generate personalized email using Groq API
def generate_personalized_email(name, expectations):
    print("[Engagement Agent] Generating personalized email...")
    prompt = f"""
    Write a professional email addressing {name} based on their expectations:
    '{expectations}'. Make the email personalized, engaging, and relevant.
    Include the company name 'XYZ Limited'. 
    
    The output should follow this format:
    
    Subject: <Insert Email Subject Here>
    
    Body:
    <Insert Email Body Here>

    Ensure the email provides specific benefits or features tailored to the user's expectations.
    Additionally, provide relevant resource links that align with the user's needs.
    Links should be clickable and can be redirected.
    Also Keep name of Mail Sender as "Aaditya" with Contact Info as "aadityaxyz@gmail.com"
    Important : "Please dont repeat anything keep it clear and avoid redundancy"
    """
    
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
    )
    
    print("[Engagement Agent] Email generation completed.")
    
    email_text = response.choices[0].message.content.strip()
    
    # Extract subject and body
    subject_line = ""
    body_text = ""
    
    if "Subject:" in email_text:
        parts = email_text.split("Subject:", 1)
        subject_and_body = parts[1].strip()
        
        if "Body:" in subject_and_body:
            subject_line, body_text = subject_and_body.split("Body:", 1)
            subject_line = subject_line.strip()
            body_text = body_text.strip()
        else:
            subject_line = subject_and_body.strip()
    
    return subject_line, body_text


# Function to classify leads
def classify_lead(interest):
    print("[Sales Agent] Classifying lead...")
    if interest in ["Demo Request", "Product Inquiry"]:
        return "Hot"
    elif interest in ["Pricing Information", "Offers"]:
        return "Warm"
    else:
        return "Cold"

# Function to send email
def send_email(to_email, subject, body):
    msg = MIMEMultipart()
    msg['From'] = SENDER_EMAIL
    msg['To'] = to_email
    msg['Subject'] = subject  # Now dynamically set

    msg.attach(MIMEText(body, 'plain'))
    
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.sendmail(SENDER_EMAIL, to_email, msg.as_string())
        print("Email sent successfully!")
    except Exception as e:
        print("Failed to send email:", e)


# Process lead
def process_lead(lead_data):
    print("[Lead Generator] Processing lead...")
    if lead_data["interest"] in ["Product Inquiry", "Demo Request", "Pricing Information", "Offers"]:
        print("[Lead Generator] Lead identified, passing to Engagement Agent.")
        
        subject, body = generate_personalized_email(lead_data["name"], lead_data["expectations"])
        
        print("[Lead Generator] Passing to Sales Agent for classification.")
        lead_score = classify_lead(lead_data["interest"])
        print("[Sales Agent] Classification completed.")

        # Send email
        send_email(lead_data["email"], subject, body)

        #  Update Google Sheet after sending the email
        update_google_sheet(lead_data["name"], lead_data["email"], lead_score, lead_data["interest"])
        
        return {"email": lead_data['email'], "lead_score": lead_score, "subject": subject, "body": body}
    else:
        print("[Lead Generator] No specific interest found. Sending reminder email.")
        subject = "Just Checking In"
        body = f"""
        Dear {lead_data["name"]},

        We noticed you haven’t expressed a specific interest yet, and we’d love to help you explore our offerings.
        Let us know how we can assist you!

        Best regards,
        Aaditya
        XYZ Limited
        aadityaxyz@gmail.com
        """

         # Send reminder email
        send_email(lead_data["email"], subject, body)

        #Update Google Sheet for "Cold" leads too
        update_google_sheet(lead_data["name"], lead_data["email"], "Cold", lead_data["interest"])
        
        return {"email": lead_data["email"], "lead_score": "Cold", "subject": subject, "body": body}
        


# sample_data = {
#     'interest' : 'Pricing Information',
#     'name' : 'Madhur',
#     'email' : 'aady10748@gmail.com',
#     'expectations' : 'I want a offer',
# }

# result = process_lead(sample_data)
# print(result)
# mail = send_email(result['email'], result['subject'], result['body'])
# print(mail)