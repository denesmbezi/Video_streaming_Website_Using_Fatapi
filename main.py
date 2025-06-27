from fastapi import FastAPI
from fastapi.responses import StreamingResponse

app = FastAPI()

@app.get("/video")
def get_video():
    video_path = "path/to/your/video.mp4"
    return StreamingResponse(open(video_path, "rb"), media_type="video/mp4")
