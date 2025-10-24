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
          "content": "Bạn là một chuyên gia về phân tích và tổng hợp thông tin"
      },
      {
          "role": "user",
          "content": 
    
"Tôi sẽ gửi bạn 1 list các url các bài báo tương ứng liên quan đến tác động của AI"
"đối với kinh tế và xã hội việt nam trong năm 2025."
"sau đó, hãy tổng hợp thông tin, và số liệu ngày tháng các sự kiện chính sách (nếu có), các insight nếu có."
"sau đó, hãy viết script kịch bản (cho 6s video) gồm tổng hợp 9 video liên tiếp nhau cho 1 bản tin."
"Có thể custom lại ý tưởng cho từng video ngắn nhé."

"video 1: Xin chào quý vị và các bạn, đây là bản tin về tác động của AI đến đời sống và xã hội của việt nam trong năm 2025. Đây là sản phẩm tham dự cuộc thi AI thực chiến."
"video 2: trình bày thông tin chung"
"video 3: trình bày các sự kiện "
"video 4: trình bày các số liệu, tương ứng"
"video 5: trình bày thế mạnh của AI và tác động mạnh mẽ đến đời sống xã hội"
"video 6: trình bày về AI ảnh hưởng đến thế hệ trẻ, con người, thất nghiệp,..."
"video 7: trình bày xu hướng AI thời đại mới"
"video 8: tổng kết"
"video 9: cảm ơn, đã đồng hành cùng team D2AI tham dự cuộc thi AI thực chiến."
"List url: "
"https://dangcongsan.vn/hocvienchinhtri/xay-dung-dang/su-phat-trien-va-tac-dong-cua-tri-tue-nhan-tao-ai-nhung-co-hoi-va-thach-thuc-dat-ra-trong-cong-tac-quan-tri-quoc-gia.html"
"https://dangcongsan.vn/van-de-quan-tam/viet-nam-se-co-luat-tri-tue-nhan-tao-vao-cuoi-nam-nay.html"
"https://dangcongsan.vn/bokhoahoccongnghe/tin-tuc-hoat-dong/khai-mac-ngay-hoi-tri-tue-nhan-tao-viet-nam-2025-viet-nam-trong-cuoc-dua-ai-toan-cau.html"
"https://dangcongsan.vn/hocvienchinhtri/xay-dung-dang/tri-tue-nhan-tao-va-su-nhin-nhan-lai-ve-mo-hinh-tang-truong-kinh-te.html"
"https://dangcongsan.vn/hocvienchinhtri/xay-dung-dang/chien-luoc-phat-trien-ai-quoc-gia-tu-tam-nhin-den-hanh-dong.html"
"https://dangcongsan.vn/haiphong/tin-tuc-hoat-dong/ai-tao-sinh-xu-the-khoi-nghiep-va-phat-trien-kinh-te-so-cua-hai-phong.html"
"https://dangcongsan.vn/tphochiminh/tin-tuc-hoat-dong/de-xuat-thi-diem-thanh-lap-co-quan-bao-chi-truyen-thong-chu-luc-da-phuong-tien-o-tphcm-ha-noi.html"
"https://dangcongsan.vn/nganhangnhanuoc/tin-tuc-hoat-dong/thoi-bao-ngan-hang-va-hoc-vien-ngan-hang-phoi-hop-to-chuc-chuoi-su-kien-chao-tan-sinh-vien-2025.html"
"https://dangcongsan.vn/thainguyen/tin-tuc-hoat-dong/cau-chuyen-quoc-te-cai-gia-cua-ai-mien-phi.html"
"https://dangcongsan.vn/bokhoahoccongnghe/tin-tuc-hoat-dong/thuc-day-he-sinh-thai-ai-phat-trien-manh-me-va-co-trach-nhiem-tai-viet-nam.html"
"https://dangcongsan.vn/bokhoahoccongnghe/tin-tuc-hoat-dong/thuc-day-he-sinh-thai-ai-phat-trien-manh-me-va-co-trach-nhiem-tai-viet-nam.html"
"https://dangcongsan.vn/hocvienchinhtri/xay-dung-dang/hoi-thao-khoa-hoc-quoc-gia-suc-manh-khong-gioi-han-va-nhung-thach-thuc-kho-du-bao-cua-tri-tue-nhan-tao-tac-dong-va-ung-p.html"
"https://dangcongsan.vn/bokhoahoccongnghe/tin-tuc-hoat-dong/thuc-day-chuyen-doi-so-phat-trien-kinh-te-so-va-tri-tue-nhan-tao-kien-tao-viet-nam-hung-cuong-trong-ky-nguyen-so.html"
"https://dangcongsan.vn/bokhoahoccongnghe/tin-tuc-hoat-dong/luat-tri-tue-nhan-tao-buoc-di-chien-luoc-kien-tao-nen-tang-phap-ly-cho-thoi-dai-so.html"
"https://dangcongsan.vn/hatinh/xay-dung-dang/ung-dung-tri-tue-nhan-tao-de-nang-cao-hieu-qua-cong-tac-trong-co-quan-dang.html"
"https://dangcongsan.vn/haiphong/tin-tuc-hoat-dong/sinh-vien-viet-nam-thanh-tam-diem-chien-luoc-ai-cua-cac-tap-doan-cong-nghe.html"
"https://baochinhphu.vn/ung-dung-cong-nghe-ai-ai-nhanh-hon-nguoi-do-chien-thang-102250909112756356.htm"
"https://baochinhphu.vn/chinh-sach-ai-eu-ap-dung-quy-dinh-dau-tien-ve-ai-da-nang-10225080210125545.htm"
"https://baochinhphu.vn/nam-2030-loi-ich-kinh-te-tu-ai-co-the-len-toi-793-ty-usd-102241115164254991.htm"
"https://baochinhphu.vn/chinh-sach-ai-hinh-thanh-2-co-che-toan-cau-ve-quan-tri-ai-102250827150136045.htm"
"https://baochinhphu.vn/chinh-sach-ai-cong-bo-mot-loat-sang-kien-hop-tac-ai-khu-vuc-asean-102250813084344011.htm"
"https://baochinhphu.vn/dinh-hinh-tuong-lai-ai-khong-chi-thong-minh-ve-cong-nghe-ma-con-giau-tinh-nhan-van-102250516121206537.htm"
"https://baochinhphu.vn/phat-trien-va-ung-dung-tri-tue-nhan-tao-co-trach-nhiem-tai-viet-nam-1022402282212344.htm"
"https://baochinhphu.vn/phat-trien-tri-tue-nhan-tao-phai-lay-loi-ich-quoc-gia-nguoi-dan-lam-trung-tam-102240823171844996.htm"
"https://baochinhphu.vn/bo-khcn-thu-hut-100-chuyen-gia-gioi-tham-gia-cac-chuong-trinh-ai-trong-diem-10225062616544581.htm"
"https://baochinhphu.vn/phat-trien-ha-tang-bao-dam-chu-quyen-tri-tue-nhan-tao-quoc-gia-102251009105406649.htm"
"https://baochinhphu.vn/ai-tro-thanh-yeu-to-quyet-dinh-hieu-suat-doanh-nghiep-102250311154310006.htm"
"https://baochinhphu.vn/quang-binh-phat-dong-phong-trao-binh-dan-hoc-vu-so-102250509114317056.htm"
"https://baochinhphu.vn/hoi-tu-tri-tue-logistics-toan-cau-viet-nam-huong-toi-trung-tam-chuoi-cung-ung-xanh-10225100815001988.htm"
"https://baochinhphu.vn/pho-thu-tuong-pham-binh-minh-dien-dam-voi-bo-truong-ngoai-giao-ai-cap-102273840.htm"
"https://vtv.vn/cong-nghe/tac-dong-va-thach-thuc-cua-tri-tue-nhan-tao-ai-doi-voi-viet-nam-20250206155150933.htm"
"https://vtv.vn/vinh-danh-hoc-sinh-sinh-vien-viet-nam-trong-linh-vuc-ai-100251024103741975.htm"
"https://vtv.vn/93-doanh-nghiep-viet-nam-dung-ai-moi-ngay-da-den-luc-thiet-bi-cong-nghe-cung-phai-thich-nghi-100250930095824847.htm"
"https://vtv.vn/cong-nghe/ai-khong-chi-la-san-choi-cho-cac-ong-lon-tai-viet-nam-2025061016101921.htm"
"https://vtv.vn/ai-dang-dan-tro-thanh-ha-tang-quoc-gia-100250829201933491.htm"
"https://vtv.vn/cong-nghe/hon-1000-chuyen-gia-sap-den-viet-nam-ban-ve-ai-ban-dan-20250224161400079.htm"
"https://vtv.vn/cong-nghe/viet-nam-dang-chuyen-minh-thanh-mot-quoc-gia-hang-dau-ve-ai-va-ban-dan-20250122153656305.htm"
"https://vtv.vn/cong-nghe/ai-khong-phai-la-san-khau-cong-nghe-ma-la-tran-dia-song-con-cua-tu-duy-20250617094701379.htm"      
    }

  ]
)

print(response.choices[0].message.content)
