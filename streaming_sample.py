from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import uvicorn
import time

app = FastAPI()

async def fake_video_streamer():
    for i in range(10):
        time.sleep(0.5)
        yield b"some fake video bytes"

@app.get("/question-stream")
async def stream():
    return StreamingResponse(fake_video_streamer(), media_type='text/event-stream')

def start():
    uvicorn.run("streaming_sample:app", host="0.0.0.0", port=8000, reload=True)

if __name__ == "__main__":
    start()
