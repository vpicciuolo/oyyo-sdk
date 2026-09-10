<div align="center">

# OYYO SDK

### Python and TypeScript integration for the proprietary OYYO AI orchestration runtime

**OpenAI-Compatible APIs · OYYO Native APIs · Memory · Tools · Artifacts · Language · Media · Growth · Hardware**

[OYYO](https://oyyo.one) · [Benchmark](https://github.com/vpicciuolo/oyyo-benchmark) · [Models](https://github.com/vpicciuolo/oyyo-models) · [API Surface](./schemas/api-surface.json) · [Founder](https://github.com/vpicciuolo) · [Investors](https://oyyo.one/investors)

**Version:** `0.1.0-foundation` · **Built in the UAE 🇦🇪**

</div>

> [!IMPORTANT]
> **OYYO is proprietary technology and is not open source.** This public repository exposes selected SDK interfaces, schemas and integration examples. It does not publish or license the OYYO core runtime, orchestration engine, models or other proprietary intellectual property.

## What is OYYO SDK?

OYYO SDK is the developer-facing integration layer for OYYO.

It is designed to make OYYO accessible through familiar AI application patterns while also exposing OYYO-native capabilities for **memory, media, tools, business artifacts, growth workflows, semantic language intelligence and hardware awareness**.

The SDK currently provides foundation clients for **Python** and **TypeScript**.

## What is OYYO?

OYYO is being built as a **proprietary AI orchestration system for modern business**.

Rather than treating AI as one chatbot connected to one model, OYYO is designed to coordinate models, tools, memory, agents, multimodal capabilities and structured work through a portable runtime architecture.

The direction includes:

- local and portable AI execution
- model and backend orchestration
- persistent memory and context
- tool and agent execution
- MCP-compatible workflows
- document, spreadsheet and presentation generation
- semantic multilingual intelligence and translation
- image, audio and video workflows
- coding and technical execution
- business, research, growth and operational workflows
- hardware-aware routing and efficiency
- compatibility with familiar AI APIs where practical

OYYO's core runtime remains private and proprietary.

## API design

OYYO separates broad compatibility from native capabilities.

### Compatibility surface

| Endpoint | Direction |
| --- | --- |
| `/v1/models` | Model discovery |
| `/v1/chat/completions` | Chat-completions compatibility |
| `/v1/responses` | Response-style execution |
| `/v1/embeddings` | Embeddings compatibility |

### OYYO-native surface

| Endpoint | Capability |
| --- | --- |
| `/oyyo/v1/memory` | Persistent memory and context operations |
| `/oyyo/v1/media` | Multimodal/media operations |
| `/oyyo/v1/tools` | Tool and execution interfaces |
| `/oyyo/v1/artifacts` | Documents, spreadsheets, presentations and structured outputs |
| `/oyyo/v1/growth` | Growth, research and marketing-oriented execution |
| `/oyyo/v1/language` | Semantic language and translation capabilities |
| `/oyyo/v1/hardware` | Runtime and hardware capability discovery |

The machine-readable foundation surface is available in [`schemas/api-surface.json`](./schemas/api-surface.json).

> [!NOTE]
> The repository is at foundation version `0.1.0`. An endpoint appearing in the public schema expresses the intended integration surface; availability can depend on the OYYO runtime version and enabled capabilities.

## Python quick start

Requires Python 3.11+.

```bash
git clone https://github.com/vpicciuolo/oyyo-sdk.git
cd oyyo-sdk/python
python -m pip install -e .
```

```python
from oyyo import OYYO

client = OYYO(base_url="http://127.0.0.1:8080")

print(client.models())
```

Chat example:

```python
response = client.chat(
    model="your-model",
    messages=[
        {"role": "user", "content": "Analyze this business problem."}
    ],
)

print(response)
```

OYYO-native memory example:

```python
result = client.memory(
    action="store",
    content="Customer prefers concise executive summaries."
)

print(result)
```

## TypeScript quick start

The TypeScript package is currently a repository-local foundation package.

```bash
git clone https://github.com/vpicciuolo/oyyo-sdk.git
cd oyyo-sdk/typescript
npm install
npm run typecheck
```

```ts
import { OYYO } from "./src/index";

const client = new OYYO({
  baseUrl: "http://127.0.0.1:8080"
});

console.log(await client.models());
```

Chat example:

```ts
const result = await client.chat({
  model: "your-model",
  messages: [
    { role: "user", content: "Analyze this business problem." }
  ]
});

console.log(result);
```

## Repository map

```text
oyyo-sdk/
├── python/      Python client, package metadata and examples
├── typescript/  TypeScript client foundation
├── schemas/     Machine-readable API surface
└── VERSION      SDK version
```

## OYYO public engineering ecosystem

| Repository | Purpose |
| --- | --- |
| **[oyyo-sdk](https://github.com/vpicciuolo/oyyo-sdk)** | Python and TypeScript integration surface for OYYO |
| **[oyyo-benchmark](https://github.com/vpicciuolo/oyyo-benchmark)** | Independent evaluation, qualification methodology and reproducible metrics |
| **[oyyo-models](https://github.com/vpicciuolo/oyyo-models)** | Model manifests, compatibility metadata, model cards, provenance and release-gate records |

These repositories provide a public technical surface around OYYO while the **core runtime, orchestration engine and proprietary implementation remain private**.

## Why the compatibility layer matters

A practical AI platform should not force developers to rewrite every integration before they can evaluate it.

OYYO therefore uses familiar API shapes where they make sense, while reserving `/oyyo/v1/...` for capabilities that go beyond generic model inference. This creates a migration path for existing AI applications without reducing OYYO to a thin wrapper around another provider.

## Project status

OYYO SDK is currently at **foundation version `0.1.0`**. Interfaces will evolve as the runtime, benchmark qualification and product surface mature.

For OYYO model metadata and release qualification, see **[oyyo-models](https://github.com/vpicciuolo/oyyo-models)** and **[oyyo-benchmark](https://github.com/vpicciuolo/oyyo-benchmark)**.

## Ownership and rights

**Copyright © 2026 OYYO · HRN INNOVATION TECHNOLOGIES LTD. All rights reserved.**

OYYO is proprietary technology. Unless an individual file explicitly states otherwise, no license to use, copy, modify, distribute, sublicense or create derivative works is granted merely because material is visible in this public repository.

---

<div align="center">

**OYYO · AI orchestration for real work · Built in the UAE 🇦🇪**

[Website](https://oyyo.one) · [Benchmark](https://github.com/vpicciuolo/oyyo-benchmark) · [Models](https://github.com/vpicciuolo/oyyo-models) · [Founder](https://github.com/vpicciuolo)

</div>
