# HuggingFace Serving Using MLRUN

## Overview
Serves a Hugging Face text-classification model using MLRun

## Setup
1. Clone repo
2. Install dependencies `pip install -r requirements.txt`
3. Configure secrets in MLRun (HF_TOKEN, API_KEY)
4. Deploy using `scripts/deploy.sh`

## Usage
Send POST request to serving endpoint with JSON: `{"text": "your input text"}`