# AI Support Intelligence

A Streamlit web app that predicts the category of a customer support ticket using a trained scikit-learn text classifier. The app shows the most likely category and the model's probabilities for all available categories.

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run streamlit_app.py
```

Open the local URL printed by Streamlit, usually <http://localhost:8501>.

## Deploy on Render

This repository's Dockerfile starts Streamlit and listens on Render's `PORT` environment variable (defaulting to `10000`). Create or update a Render **Web Service** using the repository and the **Docker** runtime, then deploy the latest commit.

The FastAPI service remains available in `src/app.py` for API use. The Dockerfile runs the Streamlit interface as the web service.
