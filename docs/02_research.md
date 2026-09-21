# Existing Implementation

## Goal
Avoid reinventing wheels, Identifying the smallest reliable tool for our usecase.

## Condidates evvaluated
|Project|What it does | Fit for PoC|Verdict|
|**Ollama**|Local model runner + HTTP/API|zero config, python friendly|
|llama.cpp|Bare-model inference, C++|too low-level, extra build time|Rejected|
|VLLM|High-throughput serving | GPU heavy overkill for 1 user| Rejected|
|LM Studio|GUI, open API-compitable API|GUI-centric, less scriptable|Rejected|
|HuggingFace transformer| Full control | slow cold start, more code| Rejected|

## Decision

Use **Ollama** because 
1. Single binary install, model management built in
2. Rest API `127.0.01:11434` trival to call from python
3. Supports our target models (Llma 3.2 3B QWen 2.5 0.5B) out of the box.
4. Actively maintained, huge community

## What we will build
- A thin python client
- A benchmark harness with fixed prompts
- Metrics collection (TTFT, tok/s, VRAM)


