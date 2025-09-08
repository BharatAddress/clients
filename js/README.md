![CI](https://github.com/BharatAddress/clients/actions/workflows/ci.yml/badge.svg)
![CodeQL](https://github.com/BharatAddress/clients/actions/workflows/codeql.yml/badge.svg)

# Bharat Address JS/TS Client

Build:
```bash
npm ci
npm run build
```

Usage (ESM):
```ts
import { listAddresses } from '@bharataddress/client'
const features = await listAddresses('http://localhost:8000', 10)
```

Filtering and pagination:
```ts
import { listAddresses } from '@bharataddress/client'
const features = await listAddresses('http://localhost:8000', {
  limit: 50,
  offset: 0,
  pin: '560008',
  // city, ulb_lgd, digipin, bbox also supported
})
```
