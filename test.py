import os
import time
import base64
import requests
from openai import OpenAI

# --- CẤU HÌNH ---
# Tạo thư mục để lưu các tài sản video
if not os.path.exists("video_assets"):
    os.makedirs("video_assets")

# Cấu hình client cho các API chuẩn (Chat, Image, TTS)
client = OpenAI(
  api_key="sk-zu5RN0L9XNeZf-a7ONjaoA",
  base_url="https://api.thucchien.ai"
)

# Cấu hình riêng cho API Google Veo (Video)
VEO_API_KEY = "sk-zu5RN0L9XNeZf-a7ONjaoA" # Sử dụng cùng API key
VEO_BASE_URL = "https://api.thucchien.ai"

# --- CÁC HÀM HỖ TRỢ ---

def generate_script_segments():
    """Tạo kịch bản và chia thành 3 phân đoạn."""
    print("1. Đang tạo kịch bản cho bản tin...")
    system_prompt = """
    Bạn là một biên tập viên truyền hình, viết kịch bản cho bản tin 'Tương Lai AI Việt'.
    Nhiệm vụ: Viết một kịch bản tổng thể khoảng 50-60 từ về AI Việt Nam 2025, sau đó chia nó thành 3 phần JSON riêng biệt: 'intro', 'main_point', 'conclusion'.
    Mỗi phần phải có 'id', 'text' (lời thoại), và 'visual_prompt' (gợi ý hình ảnh/video).
    """
    user_prompt = "Hãy tạo kịch bản 20 giây về sự phát triển AI tại Việt Nam, tập trung vào các ứng dụng trong nông nghiệp công nghệ cao."
    
    response = client.chat.completions.create(
        model="gemini-2.5-pro",
        messages=[{"role": "system", "content": system_prompt}, {"role": "user", "content": user_prompt}],
        temperature=0.7
    )
    script_text = response.choices[0].message.content
    
    # Giả lập việc phân tách JSON từ text trả về (vì API có thể không trả về JSON hoàn hảo)
    # Trong thực tế, bạn cần parse chuỗi JSON này một cách cẩn thận
    script_segments = [
        {"id": 1, "text": "Xin chào, tôi là Minh Anh. Năm 2025 chứng kiến trí tuệ nhân tạo thay đổi bộ mặt nông nghiệp Việt Nam.", "visual_prompt": "MC Minh Anh nói trong studio ảo."},
        {"id": 2, "text": "Các drone tự hành và cảm biến thông minh đang tối ưu hóa mùa màng, mang lại hiệu quả vượt trội.", "visual_prompt": "Drone AI bay trên cánh đồng lúa xanh mướt tại đồng bằng sông Cửu Long."},
        {"id": 3, "text": "Đây là bước nhảy vọt, khẳng định vị thế công nghệ của nước nhà. Xin cảm ơn và hẹn gặp lại.", "visual_prompt": "MC Minh Anh mỉm cười và kết thúc bản tin."}
    ]
    print("   -> Kịch bản đã được tạo và chia thành 3 phần.\n")
    return script_segments

def generate_tts_audio(segment):
    """Tạo file audio từ văn bản."""
    print(f"3. Đang tạo giọng đọc cho phần {segment['id']}...")
    response = client.audio.speech.create(
        model="gemini-2.5-flash-preview-tts",
        input=segment['text'],
        voice="Zephyr"
    )
    file_path = f"video_assets/audio_{segment['id']}.mp3"
    response.stream_to_file(file_path)
    print(f"   -> Đã lưu giọng đọc tại: {file_path}\n")

def generate_mc_image():
    print("2. Đang tạo hình ảnh MC ảo 'Minh Anh'...")
    response = client.chat.completions.create(
        model="gemini-2.5-flash-image-preview",
        messages=[{
            "role": "user",
            "content": "Tạo hình ảnh một nữ MC ảo người Việt tên 'Minh Anh', khoảng 30 tuổi, phong cách chuyên nghiệp, thông minh, mặc áo dài cách tân màu xanh đậm, trong một studio tin tức ảo tương lai."
        }],
        modalities=["image"]
    )
    
    # Trích xuất dữ liệu base64 từ cấu trúc phản hồi mới
    # Ví dụ: 'data:image/png;base64,iVBORw0KGgo...'
    image_url = response.choices[0].message.images[0].image_url.url
    b64_data = image_url.split(",")[1]

    file_path = "video_assets/mc_image.png"
    with open(file_path, "wb") as f:
        f.write(base64.b64decode(b64_data))
    print(f"   -> Đã lưu hình ảnh MC tại: {file_path}\n")
    return b64_data

def generate_video_clip(segment, mc_image_b64=None):
    """Tạo video clip bằng API Veo (quy trình 3 bước)."""
    print(f"4. Đang tạo video clip cho phần {segment['id']}...")
    
    # --- Bước 1: Gửi yêu cầu tạo video ---
    model = "veo-2.0-generate-001"
    url_start = f"{VEO_BASE_URL}/gemini/v1beta/models/{model}:predictLongRunning"
    
    payload = {
        "instances": [{
            "prompt": segment['visual_prompt'],
            "parameters": {"durationSeconds": 7, "aspectRatio": "16:9"}
        }]
    }
    if mc_image_b64:
        payload["instances"][0]["image"] = {
            "bytesBase64Encoded": mc_image_b64,
            "mimeType": "image/png"
        }

    headers = {"x-goog-api-key": VEO_API_KEY, "Content-Type": "application/json"}
    
    try:
        response_start = requests.post(url_start, json=payload, headers=headers)
        response_start.raise_for_status()
        operation_name = response_start.json()['name']
        print(f"   -> Đã gửi yêu cầu, Tên tác vụ: {operation_name}")
    except requests.exceptions.RequestException as e:
        print(f"   !!! Lỗi khi bắt đầu tác vụ video: {e}")
        print(f"   -> Phản hồi từ server: {response_start.text}")
        return

    # --- Bước 2: Kiểm tra trạng thái ---
    url_check = f"{VEO_BASE_URL}/{operation_name}"
    while True:
        print("   -> Đang kiểm tra trạng thái...")
        response_check = requests.get(url_check, headers=headers)
        status = response_check.json()
        if status.get('done'):
            print("   -> Tác vụ đã hoàn thành!")
            video_uri = status['response']['uri']
            break
        time.sleep(10) # Chờ 10 giây trước khi kiểm tra lại

    # --- Bước 3: Tải video ---
    video_id = video_uri.split('/')[-1].split(':')[0]
    url_download = f"https://api.thucchien.ai/gemini/download/v1beta/files/{video_id}:download?alt=media"
    
    print(f"   -> Đang tải video từ ID: {video_id}...")
    response_download = requests.get(url_download, headers=headers)
    
    file_path = f"video_assets/video_{segment['id']}.mp4"
    with open(file_path, "wb") as f:
        f.write(response_download.content)
    print(f"   -> Đã lưu video tại: {file_path}\n")

# --- QUY TRÌNH CHÍNH ---
if __name__ == "__main__":
    # 1. Tạo kịch bản
    script_segments = generate_script_segments()
    
    # 2. Tạo hình ảnh MC
    mc_image_base64 = generate_mc_image()

    # 3. Tạo giọng đọc và video cho từng phần
    for seg in script_segments:
        generate_tts_audio(seg)
        if "MC" in seg['visual_prompt']:
            # Tạo video có MC
            generate_video_clip(seg, mc_image_b64=mc_image_base64)
        else:
            # Tạo video B-roll (không có MC)
            generate_video_clip(seg)
            
    print("--- HOÀN TẤT TẠO TÀI SẢN VIDEO ---")
    print("Tất cả các tệp audio và video đã được lưu trong thư mục 'video_assets'.")
    print("Bước tiếp theo: Dùng phần mềm chỉnh sửa video để ghép các tệp sau theo thứ tự:")
    print("1. video_1.mp4 + audio_1.mp3")
    print("2. video_2.mp4 + audio_2.mp3")
    print("3. video_3.mp4 + audio_3.mp3")
