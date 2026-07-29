# AsterSurge

Open-source AI infrastructure for building intelligent software..

## Features

- 🤖 Multi-provider LLM support
  - Groq
  - OpenAI
  - Google Gemini
  - Ollama

- 🧠 Persistent conversation memory

- 🔌 Plugin system

- 🛠 Built-in tools

- ⚡ FastAPI server

- 💻 Command-line interface

- 📦 Installable Python package

---

## Installation

Clone the repository:

```bash
git clone https://github.com/prakharsrivastavadev/AsterSurge.git
cd AsterSurge
```

Install:

```bash
pip install -e .
```

Or:

```bash
pip install -r requirements.txt
```

---

## Environment

Copy:

```text
.env.example
```

to

```text
.env
```

and configure your API keys.

Example:

```env
GROQ_API_KEY=your_key
OPENAI_API_KEY=your_key
GEMINI_API_KEY=your_key
```

---

## CLI

```bash
astersurge version
```

```bash
astersurge providers
```

```bash
astersurge config
```

```bash
astersurge chat "Hello!"
```

---

## API

Run:

```bash
uvicorn astersurge.api:app --reload
```

Open:

```
http://127.0.0.1:8000/docs
```

---

## Supported Providers

- Groq
- OpenAI
- Google Gemini
- Ollama

---

## Project Structure

```text
src/
└── astersurge/
```

---

## License

MIT License
