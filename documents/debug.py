import litellm

# --- Cấu hình ---
litellm.api_base = "https://api.thucchien.ai"

# --- Thực thi ---
response = litellm.completion(
  model="gemini-2.5-flash",
  messages=[
      {
          "role": "system",
          "content": "Bạn là một chuyên gia sửa lỗi code"
      },
      {
          "role": "user",
          "content": "  import google.auth as google_auth ModuleNotFoundError: No module named 'google'"
      }
  ],
  api_key="sk-zu5RN0L9XNeZf-a7ONjaoA"
)

print(response.choices[0].message.content)