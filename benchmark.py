import csv
import requests
import time

# Configuration
API_URL = "http://localhost:8000/evaluate"
DATA_FILE = "benchmark_data.csv"

def run_benchmark():
    print(f"Starting benchmark using data from {DATA_FILE}...")
    
    total_requests = 0
    positive_count = 0
    start_time = time.time()

    try:
        with open(DATA_FILE, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            
            for row in reader:
                text = row['text']
                total_requests += 1
                
                # Send the request to your Docker container
                response = requests.post(API_URL, json={"text": text})
                
                if response.status_code == 200:
                    result = response.json()
                    label = result['label']
                    score = result['score']
                    
                    # Track positive outcomes
                    if label == "POSITIVE":
                        positive_count += 1
                        
                    print(f"Tested: '{text[:60]}...' -> {label} ({score:.2f})")
                else:
                    print(f"Error evaluating: '{text[:60]}...' - Status Code: {response.status_code}")

    except FileNotFoundError:
        print(f"Error: Could not find {DATA_FILE}. Make sure it is in the same folder.")
        return
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to the API. Is your Docker container running?")
        return

    # Calculate final benchmark metrics
    end_time = time.time()
    total_time = end_time - start_time
    positive_percentage = (positive_count / total_requests) * 100 if total_requests > 0 else 0

    print("\n" + "="*40)
    print("🏆 BENCHMARK RESULTS 🏆")
    print("="*40)
    print(f"Total Interactions Evaluated: {total_requests}")
    print(f"Overall User Sentiment:       {positive_percentage:.1f}% POSITIVE")
    print(f"Total Benchmark Time:         {total_time:.2f} seconds")
    print(f"Average Latency per Request:  {(total_time / total_requests) * 1000:.1f} ms")
    print("="*40)

if __name__ == "__main__":
    run_benchmark()