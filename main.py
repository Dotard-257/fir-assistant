from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI(title="FIR Filing Assistant")

# This allows the browser to talk to the backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# When someone opens http://localhost:8000 — serve the HTML file
@app.get("/")
def home():
    return FileResponse("index.html")

# Police stations by district — add more as needed
@app.get("/stations/{district}")
def get_stations(district: str):
    stations = {
        "west tripura": [
            {"name": "West Agartala Police Station",  "phone": "0381-2325xxx", "type": "General"},
            {"name": "East Agartala Police Station",   "phone": "0381-2320xxx", "type": "General"},
            {"name": "Women Police Station Agartala",  "phone": "0381-2322xxx", "type": "Women"},
            {"name": "Cyber Crime Cell Tripura",       "phone": "1930",         "type": "Cyber"},
        ],
        "north tripura": [
            {"name": "Dharmanagar Police Station",     "phone": "03822-22xxxx", "type": "General"},
        ],
        "south tripura": [
            {"name": "Udaipur Police Station",         "phone": "03821-22xxxx", "type": "General"},
        ],
    }
    result = stations.get(district.lower().strip())
    if not result:
        return [{"name": "Contact local SP office or dial 100", "phone": "100", "type": "Emergency"}]
    return result


# Run the server when you execute: python main.py
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)