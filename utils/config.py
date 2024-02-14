## Run the model

import transformers
print(transformers.__path__)

from transformers import AutoModelForCausalLM, AutoTokenizer #Original Import name = AutoModelForCausalLM

model_id = "mistralai/Mixtral-8x7B-v0.1"
tokenizer = AutoTokenizer.from_pretrained(model_id)

model = AutoModelForCausalLM.from_pretrained(model_id)

text = input("Say Something")
inputs = tokenizer(text, return_tensors="pt")

outputs = model.generate(**inputs, max_new_tokens=50)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))

