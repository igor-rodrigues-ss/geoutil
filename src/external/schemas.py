from pydantic import BaseModel


class SeachIPResponseSchema(BaseModel):
    hostname: str
    country: str
    region: str
    city: str
    loc: str
    org: str

    class Config:
        schema_extra = {
            "hostname": "192-123-54-44.user3p.brasiltelecom.net.br",
            "country": "BR",
            "region": "Federal District",
            "city": "Brasília",
            "loc": "-15.8451,-47.5035",
            "org": "AS8167 OI S.A. - EM RECUPERACAO JUDICIAL",
        }
