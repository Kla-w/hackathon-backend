import uvicorn

from zerodapi.main import app

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=5000, log_level="info")
    # uvicorn.run(app, host="127.0.0.1", port=5000, debug=True, reload=True, log_level="info")
