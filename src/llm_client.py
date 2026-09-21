import json 
from dataclasses import dataclass
import time
from typing import Iterator

import requests

OLLAMA_URL = ""

@dataclass
class GenerationResult:
    prompt: str
    response: str
    ttft_s: float
    total_s: float
    tokens: int
    tokens_per_sec: float

def Stream_generate(prompt:str, model:str="llma3.2:3b")->Iterator[dict]:
    payload = {
        "model": model, "prompt": prompt, "stream": True
    }

    with requests.post(OLLAMA_URL, json=payload, stream=True, timeout=300) as r:
        r.raise_for_status()
        for line in r.iter_lines():
            if line:
                yield json.loads(line)

def generate(prompt:str, model:str="llama3.2:3b")->GenerationResult:
    start = time.perf_counter()
    ttft = None
    chunks:list[str] = []
    tokens = 0

    for chunk in Stream_generate(prompt, model=model):
        if ttft is None and chunk.get("response"):
            ttft = time.perf_counter() - start

        if chunk.get("response"):
            chunks.append(chunk["response"])
            tokens += 1
        if chunk.get("done"):
            break

    total = time.perf_counter() - start

    return GenerationResult(
        prompt=prompt,
        response="".join(chunks),
        ttft_s=ttft or -0.1,
        total_s = total,
        tokens = tokens,
        token_per_sec = (tokens/total) if total > 0 else 0.0
    )



if __name__ == "__main__":
    result = generate("Explain a proof of conceptin one sentence")
    print(f"TTFT: {result.ttft_s:.2f}s | {result.tokens_per_sec:.2f} tok/s")
    print(f"Response: {result.response.strip()}")
