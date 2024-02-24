import openai

openai.api_key = "Your API-KEY"

chat_log = []
while true:
  user_message = input("User: ")
  break
else:
  chat_log.append({"role": "user", "content": user_message})
  response = openai.chat.completions.create()





