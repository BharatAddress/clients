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
