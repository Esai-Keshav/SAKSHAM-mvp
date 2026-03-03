# Use official uv image
FROM ghcr.io/astral-sh/uv:python3.10-bookworm

WORKDIR /app

COPY requirements.txt .

RUN uv pip install --system -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["chainlit", "run", "ui.py", "--host", "0.0.0.0", "--port", "8000"]