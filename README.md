# SAKSHAM MVP

## Installation

1. Clone the repository:
   ```bash
   git clone <repo-url>
   cd SAKSHAM-mvp
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up your environment variables in a `.env` file as needed.

## Running the Application

Start the Chainlit UI:

```bash
chainlit run ui.py
```

## Features

- Strict support for Google Pixel and iOS 18 devices
- Scam and financial topic override responses
- Device verification before troubleshooting
- Uses PostgreSQL for chat and vector storage
- LangChain-powered LLM and embeddings

## Notes

- Ensure PostgreSQL is running and accessible with the credentials in `config.py`.
- Adjust model and database settings in `config.py` as needed.
