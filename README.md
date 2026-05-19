# 🏎️ GenAI Evaluator & Benchmarking API

A lightweight, containerized API built to automatically benchmark and evaluate Natural Language Processing (NLP) models. This project simulates an automated evaluation pipeline for Generative AI systems, mimicking the "LLM-as-a-judge" or quantitative evaluation workflows used in production environments.

## 📌 Overview
Evaluating Generative AI outputs manually is unscalable. This project provides a programmatic way to test an AI's responses at scale. It serves a pre-trained Hugging Face Transformer model via **FastAPI**, containerizes the environment using **Docker**, and includes a Python benchmarking script to hammer the API with simulated user interactions and calculate aggregate performance metrics.

## 🚀 Key Features
* **Containerized Deployment:** Fully reproducible environment using Docker.
* **FastAPI Backend:** High-performance, asynchronous REST API for model inference.
* **Hugging Face Integration:** Utilizes the `transformers` library for out-of-the-box sentiment classification.
* **Automated Benchmarking:** A custom script (`benchmark.py`) that reads test cases from a CSV, evaluates them against the API, and generates a performance report (latency, success rate, sentiment accuracy).

## 🛠️ Tech Stack
* **Language:** Python 3.9+
* **Framework:** FastAPI, Uvicorn
* **Machine Learning:** PyTorch, Hugging Face `transformers`
* **Infrastructure:** Docker

## 📂 Project Structure
```text
docker-ai-evaluator/
├── app.py                 # FastAPI application and model loading
├── benchmark.py           # Automated evaluation script
├── benchmark_data.csv     # Simulated user interaction dataset
├── Dockerfile             # Container configuration
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation