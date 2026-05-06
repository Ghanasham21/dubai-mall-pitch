from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import uvicorn

app = FastAPI(title="The Dubai Mall Pitch Deck")

# Mounts the static folder so the browser can see your video
app.mount("/static", StaticFiles(directory="static"), name="static")

# Points to your HTML file
templates = Jinja2Templates(directory="templates")

# Your updated content dictionary
content_data = {
    "hero": {
        "headline": "Not a Mall.",
        "subheadline": "A Global Destination.",
        "videoUrl": "/static/dubai-fountain.mp4" 
    },
    "demographics": {
        "title": "The Center of the World",
        "stats": [
            { "value": "80M+", "label": "Annual Visitors" },
            { "value": "1,200", "label": "Retail Flagships" },
            { "value": "5.9M", "label": "Square Feet of Commerce" }
        ]
    }
}

@app.get("/")
async def read_deck(request: Request):
    # The updated strict syntax required by the new FastAPI version
    return templates.TemplateResponse(
        request=request,
        name="index.html", 
        context={"content": content_data}
    )

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)