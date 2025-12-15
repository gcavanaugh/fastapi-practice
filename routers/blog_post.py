from fastapi import APIRouter, Path, Query, Body
from pydantic import BaseModel
from typing import Optional, List

router = APIRouter(
    prefix="/blog",
    tags=["blog"]
)

class ImageModel(BaseModel):
    url: str
    alias: Optional[str] = None
    
class BlogModel(BaseModel):
    title: str
    content: str
    published: Optional[bool] = True
    tags: Optional[List[str]] = []
    image: Optional[ImageModel] = None

@router.post('/new/{id}')
def create_blog(blog: BlogModel, id: int, version: int = 1):
    return {
        'id': id,
        'version': version,
        'message': 'Blog created successfully',
        'blog': blog
    }
    
@router.post('/new/{id}/comments/{comment_id}')
def create_blog_comment(id: int, 
                        comment_title: str = Query(
                            None, 
                            description="The comment title for the blog post",
                            alias="commentTitle"
                            ), 
                        comment_text: str = Body(
                            Ellipsis,
                            description="The text of the comment",
                            regex="^[a-z/s]*$"
                                ),
                        v: Optional[List[str]] = Query(None),
                        comment_id: int = Path(..., gt=21, lt=99)
                        ):
    return {
        'blog_id': id,
        'message': 'Comment added successfully',
        'comment_id': comment_id,
        'comment_text': comment_text
    }

def required_functionality():
    return {"message": "This is required functionality"}