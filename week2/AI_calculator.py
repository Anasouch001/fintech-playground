from llama_helper import ask_llama

mad = float(input("Enter MAD amount: "))
response = ask_llama(f"Convert {mad} MAD to USD. Return only a number.")
print(f"≈ {float(response):.2f} USD")
