<div align="center">

# 🧰 MCP Client

### AI-Powered Multi-Server MCP Client

Connect Local & Remote MCP Servers using LangChain, Streamlit and OpenRouter

<p align="center">
<img src="https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge">
<img src="https://img.shields.io/badge/FastMCP-3.x-success?style=for-the-badge">
<img src="https://img.shields.io/badge/LangChain-Latest-orange?style=for-the-badge">
<img src="https://img.shields.io/badge/OpenRouter-AI-purple?style=for-the-badge">
<img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge">
</p>

</div>

---

# ✨ Features

- 🔌 Connect multiple MCP servers simultaneously
- 🤖 AI Agent powered by LangChain
- 🌍 Supports Local & Remote MCP Servers
- ⚡ OpenRouter Integration
- 🎯 Dynamic Tool Discovery
- 💬 Streamlit Chat Interface
- 🔄 Automatic Tool Invocation
- 📦 Modular Architecture

---

# 📸 Demo

<p align="center">

Add your GIF here

</p>

---

# 🏗 Architecture

```text
                User
                 │
                 ▼
          Streamlit Chat UI
                 │
                 ▼
           LangChain Agent
                 │
      ┌──────────┴──────────┐
      │                     │
      ▼                     ▼
 Local MCP            Remote MCP
 (Math Server)     (Expense Server)
      │                     │
      └──────────┬──────────┘
                 ▼
            Tool Responses
                 ▼
             Final Answer
```

---

# 🚀 Tech Stack

- Python
- FastMCP
- LangChain
- Streamlit
- OpenRouter
- OpenAI Compatible APIs

---

# 📁 Project Structure

```text
MCPCLIENT/
│
├── client.py
├── main.py
├── main2.py
├── pyproject.toml
├── uv.lock
└── README.md
```

---

# ⚙ Installation

```bash
git clone https://github.com/yourusername/MCP-client.git

cd MCP-client

uv sync
```

---

# 🔑 Environment Variables

```env
OPENROUTER_API_KEY=your_key_here
```

---

# ▶ Run

```bash
streamlit run client.py
```

---

# 🧩 Supported MCP Servers

| Server | Status |
|----------|--------|
| Local Math MCP | ✅ |
| Expense Tracker MCP | ✅ |
| Future MCP Servers | 🚀 |

---

# 🌟 Roadmap

- Authentication
- Memory
- Multi-Agent Support
- Voice Interaction
- Image Understanding
- RAG Integration
- Agentic Workflow

---

# 🤝 Contributing

Pull Requests are welcome!

---

# 📄 License

MIT
