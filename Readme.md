# ✍️ YouTube Video to Blog Writer

Convert **YouTube videos** or **channels** into well-written blog posts using the power of AI.

🚀 **Live Demo**: [blog-writer-app-production.up.railway.app](https://blog-writer-app-production.up.railway.app)

---

## 📌 Features

- 🎥 Accepts both YouTube **video URLs** and **channel URLs**
- 🧠 Extracts content using transcription
- 📝 Generates a well-structured blog post using LLMs
- 📦 Dockerized for easy deployment
- ☁️ Hosted on Railway



---

## 🚀 How It Works

1. Enter a YouTube **video link** or **channel link**
2. Click "Generate Blog"
3. The app fetches transcript → summarizes content → converts to blog

---

## 🧰 Tech Stack

- **Frontend**: Streamlit
- **Backend**: Python
- **LLM**: Groq
- **Deployment**: Railway
- **Containerization**: Docker

---

## 🐳 Docker Setup

```bash
# Clone the repo
git clone https://github.com/srsuveer1807/Youtube-Video-to-Blog.git
cd Youtube-Video-to-Blog

# Build Docker image
docker build -t blog-writer-app .

# Run container
docker run -p 8501:8501 blog-writer-app
