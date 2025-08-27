import requests
from typing import List, Optional
from .models import AddressFeature


class BharatAddressClient:
    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip("/")

    def list_addresses(self, limit: int = 100) -> List[AddressFeature]:
        url = f"{self.base_url}/collections/addresses/items"
        resp = requests.get(url, params={"limit": limit}, timeout=30)
        resp.raise_for_status()
        data = resp.json()
        features = [AddressFeature(**f) for f in data.get("features", [])]
        return features
