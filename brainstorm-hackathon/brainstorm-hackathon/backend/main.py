from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import io
import base64

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Welcome to Brainstorm Neuroscience Hackathon API"}

@app.get("/generate_plot")
async def generate_plot():
    # Generate sample data
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    
    # Create plot
    plt.figure(figsize=(10, 6))
    plt.plot(x, y)
    plt.title("Sample Neuroscience Data")
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    
    # Save plot to bytes buffer
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    
    # Encode plot as base64 string
    plot_base64 = base64.b64encode(buffer.getvalue()).decode()
    
    return {"plot": plot_base64}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
