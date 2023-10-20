from src.database.database import base_manager
from src.review.models import ReviewInput, ReviewOutput

def get_review(id: int):
    result = base_manager.execute('SELECT * FROM review WHERE id=?', args=(id,))
    if not result:
        return None
    review = result['data']
    review_output = ReviewOutput(id=review[0], id_exhibition=review[1], id_visitor=review[2], rating=review[3], comment=review[4])
    return review_output

def add_review(new_review: ReviewInput):
    review = base_manager.execute('INSERT INTO review (id_exhibition, id_visitor, rating, comment)'
                                   'VALUES (?, ?, ?, ?)', args=(new_review.id_exhibition, new_review.id_visitor, new_review.rating, new_review.comment))

def update_review(review_id: int, new_review: ReviewInput):
    review = base_manager.execute('UPDATE review SET id_exhibition=?, id_visitor=?, rating=?, comment=?  WHERE id=?', args=(new_review.id_exhibition, new_review.id_visitor, new_review.rating, new_review.comment,review_id))

def delete_current_review(review_id: int):
    review = base_manager.execute('DELETE FROM review WHERE id=? ', args=(review_id,))