# Hypothesis & Success Criteria

## Hypothesis

- local LLM inference on consumer hardware (RTX4060)
- [usecase] with < 2h time-to-first token 
- and >= 15 token/sec generation at zero marginal cost per request


## Success Metrics
|Metric|Target|why it matters|
|------|------|--------------|
|Time to first token|<2.05|Interactive feel|
|generation throught|>= 15 tokens|Usable for real world|
|Peak VRAM usage|<7.5 GB|Must fit RTX 4060 8GB with headroom|
|Quality on 10-prompt end set| >= 80% pass |output must be useful, not just fast|
|cold start model load time|<30s|acceptable dev-loop friction|


## Scope Boundaries
**In Scope:**
- Single user, single model, single GPU
- Ollama + One small model (<= 4GB params)
- Python client via local HTTP API
- Batch of 10 fixed benchmark prompts

**Out of Scope:**
- Multi-user/concurrent requests
- Fine-tuning or quantization tuning
- Web UI, auth deployment

## Kill Criteria
- TTFT > 5s ok throughput < 5 token/s on 3B model not viable for interactive use
- VRAM overflow -> model can't run on target hardware
- output quality unusable on >50% of eval prompts

