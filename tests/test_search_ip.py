from unittest import mock
from unittest.mock import MagicMock, AsyncMock

from fastapi import status
from fastapi.testclient import TestClient as ClientTest


class TestSearchIP:
    @mock.patch("src.external.views.client", new_callable=AsyncMock)
    def test_search_ip_success(self, m_client: AsyncMock, client: ClientTest):
        expected = {
            "hostname": "192-168-10-12.user3p.brasiltelecom.net.br",
            "country": "BR",
            "region": "Federal District",
            "city": "Brasília",
            "loc": "-15.8451,-47.5035",
            "org": "AS7018 AT&T Services, Inc.",
            "bogon": False,
        }
        m_resp = MagicMock()
        m_resp.json.return_value = {"ip": "192.168.10.12", **expected}
        m_client.get.return_value = m_resp

        response = client.get("/external/ip?address=192.168.10.12")

        assert response.status_code == status.HTTP_200_OK
        assert m_client.get.call_count == 1
        assert response.json() == expected

    def test_search_ip_bad_request(self, client: ClientTest):
        response = client.get("/external/ip?address=xyzabc")

        assert response.status_code == status.HTTP_400_BAD_REQUEST
