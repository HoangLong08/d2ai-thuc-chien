import litellm

# --- Cấu hình ---
litellm.api_base = "https://api.thucchien.ai"

# --- Thực thi ---
response = litellm.completion(
  model="gemini-2.5-flash",
  messages=[
      {
          "role": "system",
          "content": "Bạn là một chuyên gia về lĩnh vực crawl dữ liệu"
      },
      {
          "role": "user",
          "content": "Tìm danh sách các bài báo liên quan đến tác động của AI hoặc trí tuệ nhân tạo trong đời sống và kinh tế xã hội việt nam từ tháng 1/2025 đến 10/2025. Các trang báo bắt buộc tham chiếu (Đảng Cộng Sản (dangcongsan.vn), Chính phủ (https://baochinhphu.vn/ ), và VTV (https://vtv.vn/ ) ."
      }
  ],
  api_key="sk-zu5RN0L9XNeZf-a7ONjaoA"
)

print(response.choices[0].message.content)