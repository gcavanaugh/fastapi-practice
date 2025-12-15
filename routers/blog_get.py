from routers.blog_post import required_functionality
from fastapi import APIRouter, status, Response, Depends
from typing import Optional
from enum import Enum 

router = APIRouter(
    prefix="/blog", 
    tags=["blog"]
)

@router.get(
    "/all", 
    summary="Retrieve all blogs",
    description="This endpoint retrieves all blog posts with optional pagination parameters.",
    response_description="List of all blog posts"
    )
def get_all_blogs(page : int = 1, page_size : Optional[int] = 10):
    return {'message': f'All blogs on page {page} with page size {page_size}'}

@router.get("/{id}/comments/{comment_id}", tags=["comments"])
def get_blog_comment(
    id: int,
    comment_id: int,
    valid: bool = True,
    username: Optional[str] = None,
    req_param: dict = Depends(required_functionality)
):
    """
    Get a specific comment for a blog post.
    - **id**: The ID of the blog post
    - **comment_id**: The ID of the comment
    - **valid**: Whether the comment is valid (default is True)
    - **username**: The username of the commenter (optional)
    """
    return {
        'message': f'Blog id: {id}, Comment id: {comment_id}, Valid: {valid}, Username: {username}',
        'req_param': req_param
    }

class BlogType(str, Enum):
    short = "short"
    story = "story"  
    howto = "howto"
    
@router.get("/type/{type}")
def get_blog_type(type : BlogType):
    return {'message': f'Blog type: {type}'}

@router.get("/{id}", status_code=status.HTTP_200_OK)
def get_blog(id : int, response : Response):
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'message': f'Blog with id: {id} not found'}
    else:
        response.status_code = status.HTTP_200_OK
        return {'message': f'Blog with id: {id}'} 
