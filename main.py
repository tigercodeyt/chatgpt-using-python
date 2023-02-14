import time
import openai

# Set up your OpenAI API key
openai.api_key = "YOUR_API_KEY"
print("\n");
# print("MADE BY MUAHMMAD ABBAS Beta (VERSION(0.1)) ")
print("="*50)
print("CHATSTAR BY TIGER CODE YT")
print("CREATED BY MUHAMMAD ABBAS")
print("="*50)
# Set the language model to use
model_engine = "text-davinci-002"

# Typewriter effect function
def typewriter_effect(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.02) # adjust the delay as needed
    print()

# Loop indefinitely
while True:
 # Print a new line before getting input from the user
    print("\n")
    # Get a question from the user as input
    prompt = input("You: ")

    # Set the maximum number of tokens to generate in the response
    max_tokens = 1024

    # Generate a response
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=max_tokens,
        temperature=0.5,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    # Print the response with typewriter effect
    response = completion.choices[0].text.strip()
    print("\n")
    typewriter_effect("ChatGPT: " + response)
