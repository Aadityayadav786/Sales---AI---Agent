# 🚀 AI-Powered Sales & Marketing Agent

## 📌 Overview
This project is an **AI-driven Sales & Marketing system** built using **CrewAI**, **Groq API**, and **Streamlit**. It automates lead generation, engagement, and classification using AI agents. The system personalizes email responses, updates CRM records, and improves sales efficiency with minimal manual effort.

## 🔥 Features
### 1️⃣ **AI Agents for Sales & Marketing**
- **Lead Generator Agent** – Filters and identifies potential leads.
- **Engagement Agent** – Crafts personalized emails based on user queries.
- **Sales Agent** – Classifies leads as **Hot, Warm, or Cold** and decides follow-up actions.

### 2️⃣ **Automated Email Generation & CRM Updates**
- **Real-time personalized emails** sent to leads based on their interests.
- **Google Sheets CRM integration** to store and track lead information.
- **Automated follow-ups** for cold leads.

### 3️⃣ **Multi-Agent Collaboration**
- CrewAI enables dynamic interaction between AI agents.
- Agents work together to streamline lead processing and engagement.

### 4️⃣ **Scalability & Deployment**
- **Built with Streamlit** for easy deployment and user interaction.
- **Deployed without GitHub dependency** (alternative hosting solutions like Streamlit Cloud, AWS, or GCP can be used).
- **Automated logs & analytics** to track performance.

## 🛠️ Tech Stack
- **Python** (Main development language)
- **CrewAI** (AI Agents Framework)
- **Groq API** (LLM for generating responses)
- **Google Sheets API** (CRM & lead management)
- **SMTP (Email Automation)** (For sending personalized emails)
- **Streamlit** (Frontend & Deployment)

## 📂 Project Structure
```
📁 sales-marketing-ai
│── 📄 agents.py        # CrewAI Agents (Lead, Engagement, Sales)
│── 📄 email_handler.py # Email automation using SMTP
│── 📄 crm_updater.py   # Google Sheets CRM integration
│── 📄 app.py           # Streamlit app for deployment
│── 📄 requirements.txt # Dependencies
│── 📄 README.md        # Project documentation
```

## 🔧 Installation & Setup
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/sales-marketing-ai.git
cd sales-marketing-ai
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Set Up Environment Variables
Create a **.env** file and add your API keys:
```
GROQ_API_KEY=your_groq_api_key
SENDER_EMAIL=your_email@gmail.com
SENDER_PASSWORD=your_email_password
```

### 4️⃣ Run the Application
```bash
streamlit run app.py
```

## 📌 Future Enhancements
- Improve **lead scoring with AI-powered analytics**.
- **Expand CRM integration** to support multiple platforms.
- Add **voice/chatbot support** for real-time sales inquiries.
- Implement **multi-agent collaboration for advanced automation**.

## 🤝 Contributing
We welcome contributions! Feel free to open issues or submit pull requests.

---
🚀 **Built with CrewAI, Groq API & Streamlit for next-gen sales automation!**
