# Chatbot Assistant with Gemini + gRPC

This project is a simple chatbot backend powered by Google's Gemini API and uses gRPC for client-server communication. It maintains context per session and provides interactive conversational experiences.

#FRAME
(project architecture)["assets/image.png"]


## 🛠 Features

- gRPC-based communication
- Google Gemini API integration
- Session-based context management
- Clean modular design (client, server, context manager, inference engine)

## 📂 Project Structure

```
assistant_backend/
│
├── assets/
│   └── image.png                # (Optional) Image asset
│
├── protos/
│   └── (Protobuf files for gRPC definitions)
│
├── assistant_pb2.py            # Generated from .proto
├── assistant_pb2_grpc.py       # Generated from .proto
├── client.py                   # gRPC client
├── server.py                   # gRPC server with Gemini integration
├── context_manager.py          # Manages chat context per session
├── inference_engine.py         # Contains the logic to generate a reply
├── requirements.txt            # Python dependencies
└── .env                        # Gemini API Key
```

## 🚀 Getting Started

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Set Up Environment

Create a `.env` file with your Gemini API key:

```
GEMINI_API=your_api_key_here
```

### 3. Run the Server

```bash
python server.py
```

### 4. Run the Client

```bash
python client.py
```

## 💡 Example Usage

```bash
Type 'exit' to stop chatting.
You: Hello
AI: I received: Hello. Previous context: 0 messages.
```

## 📌 Notes

- Ensure your `.proto` files are compiled to `assistant_pb2.py` and `assistant_pb2_grpc.py`
- Python version 3.10 or higher is recommended

## 🧠 Built With

- Python 🐍
- gRPC
- Google Gemini API
- dotenv

---

> © 2025 Om Jamnekar. All rights reserved.