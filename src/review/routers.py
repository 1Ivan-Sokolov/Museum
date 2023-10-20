from fastapi import APIRouter
from src.review.models import ReviewInput, ReviewOutput
from src.review.resolvers import add_review, get_review, delete_current_review, update_review

router = APIRouter()


@router.get('/{review}')
def get_review_router(id: int):
    return get_review(id)


@router.post('/{exhibition_review}')
def add_review_router(new_review: ReviewInput):
    return add_review(new_review)


@router.put('/{review_id}')
def update_review_router(review_id: int, new_review: ReviewInput):
    return update_review(review_id, new_review)


@router.delete('/{exhibition_review}')
def delete_current_review_router(review_id: int):
    return delete_current_review(review_id)