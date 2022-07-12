from src.external.schemas import SeachIPResponseSchema
from src.external.helper.client import client


async def search_ip(ip: str) -> SeachIPResponseSchema:
    resp = await client.get(f"https://ipinfo.io/{ip}/geo")
    return SeachIPResponseSchema(**resp.json())
