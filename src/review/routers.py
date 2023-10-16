from fastapi import APIRouter
from src.review.models import ReviewInput, ReviewOutput
from src.review.resolvers import add_review, get_review, delete_current_review, update_review

router = APIRouter()

@router.get('/{review}')
def get_review(id: int):
    return get_review()

@router.post('/{exhibition_review}')
def add_review(new_review: ReviewInput):
    return add_review()

@router.put('/{review_id}')
def update_review(review_id: int, new_review: ReviewInput):
    return update_review()

@router.delete('/{exhibition_review}')
def delete_current_review(review_id: int):
    return delete_current_review()