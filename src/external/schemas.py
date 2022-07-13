from pydantic import BaseModel
from typing import Optional


class SeachIPResponseSchema(BaseModel):
    hostname: Optional[str]
    country: Optional[str]
    region: Optional[str]
    city: Optional[str]
    loc: Optional[str]
    org: Optional[str]
    bogon: Optional[bool] = False

    class Config:
        schema_extra = {
            "example": {
                "hostname": "192-123-54-44.user3p.brasiltelecom.net.br",
                "country": "BR",
                "region": "Federal District",
                "city": "Brasília",
                "loc": "-15.8451,-47.5035",
                "org": "VIVO S.A",
                "bogon": False,
            }
        }
