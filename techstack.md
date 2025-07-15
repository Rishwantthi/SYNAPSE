# 🌾 FarmerAI: Multi-Agent AI Advisor for Small-Scale Farmers

> 🏆 Built in 24hrs at Hackfinity Agentic AI Hackathon  
> 🤖 Personalized, multilingual, farmer‑friendly AI agents

---

## 🚀 What is FarmerAI?
FarmerAI is an AI-powered multi-agent system designed to help millions of small-scale farmers:
- Decide which crops to plant (Planner Agent)
- Predict market prices & trends (Market Agent)
- Practice price negotiation (Bargain Agent)
- Identify risks & suggest fallback plans (Risk Agent)
- Answer questions about government schemes, weather & more (Info Agent)

All in **local Indian languages**: Tamil, Hindi, Telugu, etc.

---

## 🧠 **How it works**
✅ Each AI agent is built using **OpenAI GPT‑4o** with a unique system prompt  
✅ Agents first ask farmers which language to use → then reply fully in that language  
✅ Understands mixed input (e.g., crop names in Tamil) and answers in farmer-friendly words  
✅ Modular Python backend → easy to add new agents like disease detection or voice bot

---

## 🛠 **Tech Stack**
| Layer        | Tools / Libraries |
| ------------ | ----------------- |
| Frontend / UI | Streamlit (for web app) |
| AI Agents    | OpenAI GPT‑4o (via Python SDK) |
| Voice & Multilingual | Whisper / Google Translate API (optional) |
| Backend & Orchestration | Python 3.11+, `python-dotenv` |
| Data | Pandas, NumPy (for price data, CSV etc.) |
| Deployment | Replit (instant cloud), optional Streamlit Cloud |

---

## ✨ **Unique & useful**
- True **multi-agent** design (not just one chatbot)
- Local language first → inclusive for uneducated farmers
- Real-time text interface, expandable to voice & images
- Easy to scale: add weather, disease, IoT data later

---

## 📦 **Project Structure**
```plaintext
planner_agent.py     → crop planning agent
market_agent.py      → price prediction agent
bargain_agent.py     → price negotiation agent
risk_agent.py        → risk & fallback suggestions
info_agent.py        → agri Q&A helpdesk
.env                 → stores OPENAI_API_KEY
app.py / main.py     → Streamlit frontend to bring agents together
