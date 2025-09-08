![CI](https://github.com/BharatAddress/clients/actions/workflows/ci.yml/badge.svg)
![CodeQL](https://github.com/BharatAddress/clients/actions/workflows/codeql.yml/badge.svg)

# Bharat Address Python Client

Quickstart:
```bash
pip install -r requirements.txt
# or build/install package from pyproject.toml
```

Usage:
```python
from bharataddress_client import BharatAddressClient
c = BharatAddressClient("http://localhost:8000")
features = c.list_addresses(limit=10)
print(features[0])
```

Filtering and pagination:
```python
# Filter by pin / city / ulb_lgd / digipin and paginate
features = c.list_addresses(limit=50, offset=0, pin="560008")
features = c.list_addresses(city="Bengaluru")
features = c.list_addresses(bbox="77.4,12.8,77.8,13.1")
```

---
Contributor Guide: https://github.com/BharatAddress/.github/blob/main/AGENTS.md
