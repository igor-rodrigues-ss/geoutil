from fastapi import APIRouter

from src.external.views import search_ip
from src.external.schemas import SeachIPResponseSchema


router = APIRouter()


router.get("/ip", response_model=SeachIPResponseSchema)(search_ip)
