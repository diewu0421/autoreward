from openai import OpenAI
client = OpenAI(api_key="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")

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
        {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
    ]
)

print(completion.choices[0].message)