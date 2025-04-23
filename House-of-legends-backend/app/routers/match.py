from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(
    prefix="/match",
    tags=["Match"]
)

# 1. 데이터 형식 정의
class Match(BaseModel):
    team1: list[str]
    team2: list[str]
    winner: str

# 2. GET 기본 응답
@router.get("/")
def get_matches():
    return {"message": "이건 /match 라우터의 기본 응답입니다."}

# 3. POST 요청 처리
@router.post("/")
def create_match(match: Match):
    # 나중에는 여기서 DB에 저장할 예정이야
    return {
        "message": "전적이 저장되었습니다!",
        "data": match
    }
