from fastapi import APIRouter, Body
from schema import User
from DS import modelX

router = APIRouter()

@router.post('/user')
def addProduct(user: User = Body()):
    return {"msg": "User Added successfully", **user.dict()}

@router.get('/user/{id}')
def root(id: int, name: str):
    return f"User : Id is {id} and name is {name} got successfully"


@router.put('/user/{id}')
def updateProduct(id: int, name: str, user: User = Body()):
    return {"basic": f"user : Id is {id} and name is {name} updated successfully", **product.dict()}


@router.delete('/user/{id}')
def root(id: int, name: str):
    return f"user : Id is {id} and name is {name} deleted successfully"

