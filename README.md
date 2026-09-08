# OYYO SDK

Public integration surface for OYYO.

**Project:** https://oyyo.one  
**Version:** `0.1.0-foundation`

The SDK supports both an OpenAI-compatible surface and OYYO-native capabilities.

## API direction

Compatibility endpoints:

- `/v1/models`
- `/v1/chat/completions`
- `/v1/responses`
- `/v1/embeddings`

OYYO-native namespace:

- `/oyyo/v1/memory`
- `/oyyo/v1/media`
- `/oyyo/v1/tools`
- `/oyyo/v1/artifacts`
- `/oyyo/v1/growth`
- `/oyyo/v1/language`
- `/oyyo/v1/hardware`

## Python

```python
from oyyo import OYYO

client = OYYO(base_url="http://127.0.0.1:8080")
print(client.models())
```

## TypeScript

```ts
import { OYYO } from "./src/index";
const client = new OYYO({ baseUrl: "http://127.0.0.1:8080" });
console.log(await client.models());
```

The runtime server itself is developed in the private OYYO core repository until the public/private boundary is formally reviewed.
