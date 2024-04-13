import google.generativeai as genai

GOOGLE_API_KEY='AIzaSyD07p_UBclswLbm-ka8hpk8xoltbk4jEb8'
genai.configure(api_key=GOOGLE_API_KEY)

# List available models.
print('Available models:')
for m in genai.list_models():
  if 'generateContent' in m.supported_generation_methods:
      print(f'- {m.name}')
model = genai.GenerativeModel('gemini-pro')

print('\nReady to chat...')
while True:
  prompt= input("You: ")
  response = model.generate_content(prompt)
  result = ''.join([p.text for p in response.candidates[0].content.parts])
  print("Gemini: ", result)