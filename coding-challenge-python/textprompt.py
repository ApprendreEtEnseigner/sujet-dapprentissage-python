import openai

API_KEY = "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"
openai.api_key = API_KEY

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo-0301",
    messages=[
        {"role": "user", "content": "What is the difference between celcius and Farenheit"}
    ]
)

print(response)