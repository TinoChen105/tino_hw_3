import logging
import os
from typing import Any
import requests
from dotenv import load_dotenv
from libs.share_function import print_raw_http

load_dotenv()

class BaseSession(requests.Session):
    def __init__(self):
        super().__init__()
        requests.packages.urllib3.disable_warnings()
        self.adapters.DEFAULT_RETRIES = 5

    def _request(self, method: str, url: str, log: bool = True, **kwargs: Any) -> requests.Response:
        full_url = os.path.join(os.getenv("BASE_URL", ""), url)
        res = self.request(method, full_url, verify=False, **kwargs)
        if log:
            logging.debug(print_raw_http(res))
        return res

    def patch(self, url: str, log: bool = True, **kwargs: Any) -> requests.Response:
        return self._request("PATCH", url, log=log, **kwargs)

    def put(self, url: str, log: bool = True, **kwargs: Any) -> requests.Response:
        return self._request("PUT", url, log=log, **kwargs)

    def get(self, url: str, log: bool = True, **kwargs: Any) -> requests.Response:
        return self._request("GET", url, **kwargs)

    def post(self, url: str, log: bool = True, **kwargs: Any) -> requests.Response:
        return self._request("POST", url, log=log, **kwargs)

    def delete(self, url: str, log: bool = True, **kwargs: Any) -> requests.Response:
        return self._request("DELETE", url, log=log, **kwargs)
