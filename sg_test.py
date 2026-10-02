#!/usr/bin/env python3
"""Test client for the shared SGLang server (OpenAI-compatible API).

Usage:
  SG_URL=http://... SG_KEY=... python3 sg_test.py [--long]
"""
import os
import sys

from openai import OpenAI

BASE = os.environ.get("SG_URL", "https://gx10-b234.tail386c62.ts.net/v1")
KEY = os.environ.get("SG_KEY", "apexus123")

client = OpenAI(base_url=BASE, api_key=KEY, timeout=120)


def list_models():
    models = client.models.list()
    print("== /v1/models ==")
    for m in models.data:
        print(" -", m.id)
    if not models.data:
        print(" (empty)")
    return models.data[0].id if models.data else None


def chat(model, prompt, max_tokens=64):
    print(f"\n== chat with {model} ==")
    resp = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=max_tokens,
        temperature=0.2,
    )
    msg = resp.choices[0].message
    print("role:", msg.role)
    print("content:", msg.content)
    usage = getattr(resp, "usage", None)
    if usage:
        print("usage:", usage.model_dump())
    return msg.content


if __name__ == "__main__":
    model = list_models()
    if not model:
        print("No models reported; trying a default name.")
        model = "RadixArk/Qwen3.8-Flash-Next-NVFP4"
    chat(model, "Reply with exactly: SGLang is reachable.")
    if "--long" in sys.argv:
        # Push a longer prompt so the 200k context is visible in context_length.
        big = "The quick brown fox jumps over the lazy dog. " * 2000
        chat(model, big + "\n\nNow reply with only: OK", max_tokens=8)