from sqlalchemy.orm.session import Session 
from db.models import DbUser
import schemas 
from db.hash import Hash

def create_user(db: Session, request: schemas.UserBase):
    db_user = DbUser(
        username=request.username,
        email=request.email,
        password=Hash.bcrypt(request.password)
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user