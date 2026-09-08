from __future__ import annotations
import json
from urllib import request, error
from typing import Any, Optional

class OYYOError(RuntimeError):
    pass

class OYYO:
    def __init__(self, *, base_url: str = "http://127.0.0.1:8080", api_key: Optional[str] = None, timeout: float = 60.0):
        self.base_url = base_url.rstrip("/")
        self.api_key = api_key
        self.timeout = timeout

    def _request(self, method: str, path: str, payload: Optional[dict[str, Any]] = None) -> Any:
        headers = {"Accept": "application/json"}
        data = None
        if payload is not None:
            headers["Content-Type"] = "application/json"
            data = json.dumps(payload).encode("utf-8")
        if self.api_key:
            headers["Authorization"] = f"Bearer {self.api_key}"
        req = request.Request(self.base_url + path, data=data, headers=headers, method=method)
        try:
            with request.urlopen(req, timeout=self.timeout) as response:
                body = response.read()
                return json.loads(body.decode("utf-8")) if body else None
        except error.HTTPError as exc:
            detail = exc.read().decode("utf-8", errors="replace")
            raise OYYOError(f"OYYO HTTP {exc.code}: {detail}") from exc
        except error.URLError as exc:
            raise OYYOError(f"OYYO connection error: {exc.reason}") from exc

    def models(self) -> Any:
        return self._request("GET", "/v1/models")

    def chat(self, *, model: str, messages: list[dict[str, str]], **kwargs: Any) -> Any:
        payload = {"model": model, "messages": messages, **kwargs}
        return self._request("POST", "/v1/chat/completions", payload)

    def response(self, **payload: Any) -> Any:
        return self._request("POST", "/v1/responses", payload)

    def memory(self, **payload: Any) -> Any:
        return self._request("POST", "/oyyo/v1/memory", payload)

    def hardware(self) -> Any:
        return self._request("GET", "/oyyo/v1/hardware")
