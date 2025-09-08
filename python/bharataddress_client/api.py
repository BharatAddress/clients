import requests
from typing import List, Optional
from .models import AddressFeature


class BharatAddressClient:
    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip("/")

    def list_addresses(
        self,
        limit: int = 100,
        offset: int = 0,
        *,
        bbox: Optional[str] = None,
        pin: Optional[str] = None,
        city: Optional[str] = None,
        ulb_lgd: Optional[str] = None,
        digipin: Optional[str] = None,
    ) -> List[AddressFeature]:
        """List address features.

        Args:
            limit: Max number of features to return.
            offset: Pagination offset.
            bbox: Optional bbox filter as "minLon,minLat,maxLon,maxLat".
            pin: Filter by PIN code.
            city: Filter by city (case-insensitive on server).
            ulb_lgd: Filter by ULB LGD code.
            digipin: Filter by DIGIPIN (primary/secondary).
        """
        url = f"{self.base_url}/collections/addresses/items"
        params = {"limit": limit, "offset": offset}
        if bbox:
            params["bbox"] = bbox
        if pin:
            params["pin"] = pin
        if city:
            params["city"] = city
        if ulb_lgd:
            params["ulb_lgd"] = ulb_lgd
        if digipin:
            params["digipin"] = digipin
        resp = requests.get(url, params=params, timeout=30)
        resp.raise_for_status()
        data = resp.json()
        features = [AddressFeature(**f) for f in data.get("features", [])]
        return features
