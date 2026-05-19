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

```

## ⚙️ Setup & Installation

### Prerequisites

Make sure you have [Docker](https://www.docker.com/) installed and running on your machine.

### 1. Build the Docker Image

Navigate to the project directory and build the container. This will download the necessary Python base image and install all dependencies.

```bash
docker build -t ai-evaluator .

```

### 2. Run the Container

Start the API and expose it on port 8000.

```bash
docker run -p 8000:8000 ai-evaluator

```

*The API is now live at `http://localhost:8000`. You can view the interactive API documentation at `http://localhost:8000/docs`.*

## 📊 Running the Benchmark

Once the Docker container is running, you can execute the automated benchmark suite. Open a new terminal window in the project directory and run:

```bash
python benchmark.py

```

### Benchmark Results

Below is the output from a recent run against a simulated dataset of 15 in-car voice assistant interactions:

```text
Starting benchmark using data from benchmark_data.csv...
Tested: 'The new BMW voice assistant is incredibl...' -> POSITIVE (1.00)
Tested: 'The new BMW voice assistant is incredibl...' -> NEGATIVE (1.00)
Tested: 'The new BMW voice assistant is incredibl...' -> POSITIVE (1.00)
Tested: 'The new BMW voice assistant is incredibl...' -> NEGATIVE (1.00)
Tested: 'I love how quickly it changes the cabin ...' -> POSITIVE (1.00)
Tested: 'The navigation system completely misunde...' -> NEGATIVE (1.00)
Tested: 'Brilliant integration with Spotify, very...' -> POSITIVE (1.00)
Tested: 'Terrible experience, the assistant keeps...' -> NEGATIVE (1.00)
Tested: 'The voice recognition is okay, but it st...' -> NEGATIVE (1.00)
Tested: 'It takes way too long to connect to my p...' -> NEGATIVE (1.00)
Tested: 'Very intuitive menu system, I didn't eve...' -> POSITIVE (1.00)
Tested: 'It keeps interrupting me before I finish...' -> NEGATIVE (0.99)
Tested: 'Honestly, the best in-car assistant I ha...' -> POSITIVE (1.00)
Tested: 'Sometimes it answers perfectly, other ti...' -> NEGATIVE (1.00)
Tested: 'Great at finding charging stations nearb...' -> POSITIVE (1.00)

========================================
🏆 BENCHMARK RESULTS 🏆
========================================
Total Interactions Evaluated: 15
Overall User Sentiment:       46.7% POSITIVE
Total Benchmark Time:         3.10 seconds
Average Latency per Request:  206.5 ms
========================================

```

## 🔮 Future Improvements

* **LLM-as-a-Judge:** Swap the lightweight sentiment model for an API call to a larger model (e.g., GPT-4 or Llama-3) to qualitatively grade the outputs of local, in-car AI models.
* **Advanced Metrics:** Implement BLEU, ROUGE, or Perplexity scoring for generative text evaluation.
* **CI/CD Integration:** Integrate the benchmark script into GitHub Actions to block deployments if the model's accuracy drops below a defined threshold.


