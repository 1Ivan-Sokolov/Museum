from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from src.ticket.routers import router as ticket_router
from src.artwork.routers import router as artwork_router
from src.exhibition.routers import router as exhibition_router
from src.exhibit.routers import router as exhibit_router
from src.gallery.routers import router as gallery_router
from src.museum.routers import router as museum_router
from src.programm.routers import router as programm_router
from src.review.routers import router as review_router
from src.tourguide.routers import router as tourguide_router
from src.visitor.routers import router as visitor_router

app = FastAPI()

app.include_router(ticket_router, prefix="/ticket")
app.include_router(artwork_router, prefix='/artwork')
app.include_router(exhibition_router, prefix='/exhibition')
app.include_router(exhibit_router, prefix='/exhibit')
app.include_router(gallery_router, prefix='/gallery')
app.include_router(museum_router, prefix='/museum')
app.include_router(programm_router, prefix='/programm')
app.include_router(review_router, prefix='/review')
app.include_router(tourguide_router, prefix='/tourguide')
app.include_router(visitor_router, prefix='/visitor')

@app.get('/')
def root():
    return RedirectResponse('/docs')


if __name__ == '__main__':
    pass
