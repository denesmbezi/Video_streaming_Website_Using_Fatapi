from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from pydantic import BaseModel


class VideoModel(BaseModel):
    title: str
    description: str
    duration: int  # in seconds
    file_path: str



app = FastAPI()

@app.post("/video")
def create_video(video: VideoModel):
    # Here you would typically save the video metadata to a database
    return {"message": "Video created successfully", "video": video}

@app.get("/video")
def get_video():
    video_path = "path/to/your/video.mp4"
    return StreamingResponse(open(video_path, "rb"), media_type="video/mp4")
