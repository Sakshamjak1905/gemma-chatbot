import ollama

response = ollama.chat(
    model="gemma2:2b",
    messages=[{"role": "user", "content": "Say hello in one sentence"}],
)
print(response["message"]["content"])