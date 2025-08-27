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
