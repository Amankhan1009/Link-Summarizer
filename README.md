# 🦜 LangChain URL & YouTube Summarizer (Streamlit App)

This project is a **Streamlit web app** that summarizes content from **YouTube videos or website URLs** using **LangChain** and **Groq LLMs**.  
Users can paste a URL and instantly get a concise summary of the content.

---

## 🚀 Features
- 🔗 Summarize content from **YouTube videos**
- 🌐 Summarize content from **any website URL**
- 🤖 Uses **LangChain + Groq LLM**
- ⚡ Fast response using Groq API
- 🖥️ Simple and clean **Streamlit UI**
- 🔐 Secure API key input

---

## 🛠️ Tech Stack
- **Python**
- **Streamlit** – Web UI  
- **LangChain** – LLM chaining & prompts  
- **Groq API** – LLM provider  
- **YouTube Loader** – Transcript extraction  
- **UnstructuredURLLoader** – Website scraping  

---

## 📁 Project Structure
├── app.py # Main Streamlit application <br>
├── requirements.txt # Project dependencies <br>
└── README.md # Project documentation


---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

2️⃣ Create Virtual Environment (Optional but Recommended)
``` bash
python -m venv venv
venv\Scripts\activate     # Windows
# source venv/bin/activate  # Mac/Linux
```

3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```
4️⃣ Get Groq API Key

- Go to 👉 https://console.groq.com/
- Create an account
- Generate your API Key

▶️ Run the App
```bash
streamlit run app.py
```

Then open in browser:
```bash
http://localhost:8501
```

## 🧪 How to Use

1. Enter your Groq API Key
2. Paste a YouTube video URL or Website URL
3. Click "Summarize the Content from YT or Website"
4. Get the summary instantly 🎯


⚠️ Common Errors & Fixes
❌ No transcript available

Some YouTube videos don’t have captions.
👉 Try another video with subtitles enabled.

❌ Rate limit error

You may have exceeded Groq API free limits.
👉 Wait or upgrade your Groq plan.


## 📌 Example Use Cases

- Summarize long YouTube lectures

- Extract key points from blogs/articles

- Research & learning assistant

- Content preview tool


## 👨‍💻 Author

Md Aman Alam
🔗 GitHub: https://github.com/Amankhan1009

📧 Email: amankhan34356@gmail.com
