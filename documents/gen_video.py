# Cấu hình
from openai import OpenAI

client = OpenAI(
  api_key="sk-zu5RN0L9XNeZf-a7ONjaoA",
  base_url="https://api.thucchien.ai"
)

# Thực thi
response = client.chat.completions.create(
  model="gemini-2.5-flash",
  messages=[
      {
          "role": "system",
          "content": "Bạn là một để tạo prompt làm bản tin thông tin sự kiện"
      },
      {
          "role": "user",
          "content": "Tôi muốn tạo video bản tin có 1 MC đứng để trình bày về bản tin"
          "Tác động của AI đến đời sống và xã hội của Việt Nam, hãy suggest prompt phù hợp"  
    }

  ]
)

print(response.choices[0].message.content)
