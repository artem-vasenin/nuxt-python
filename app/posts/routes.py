from fastapi import APIRouter, Path, Query, Request

router = APIRouter(prefix="/posts")


@router.get("/{id}", status_code=200)
def get_post(id: int = Path(ge=10)):
    return {"post": id}


@router.get("", status_code=200)
def get_posts(limit: int = 10, offset: int = Query(0, ge=0)):
    return {"posts": [], "limit": limit, "offset": offset}


@router.post("", status_code=201)
async def add_post(resp: Request):
    return await resp.json()
