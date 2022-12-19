FROM python:3.9-slim
RUN pip3 install -r requirements.txt



EXPOSE 8501

WORKDIR /app

COPY . .



CMD ["streamlit", "run", "main.py"]