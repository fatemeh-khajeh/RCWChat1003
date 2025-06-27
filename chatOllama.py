from langchain_ollama import OllamaLLM
import time

# model = OllamaLLM(model="llama3.2")
model = OllamaLLM(model="mistral")

user_input = "Qui est Dunald Trump?"
result = model.invoke(user_input) 

for char in result:
    print(char, end="", flush=True)
    time.sleep(0.02)
print()    