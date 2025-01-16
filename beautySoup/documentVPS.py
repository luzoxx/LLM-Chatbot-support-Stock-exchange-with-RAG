import requests
from bs4 import BeautifulSoup
import csv


def crawl_website(url):
    # Gửi yêu cầu HTTP tới website
    response = requests.get(url)
    
    # Kiểm tra nếu yêu cầu thành công
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        target = soup.find('div',class_='styles_DetailPost__p0CHr DetailPost')
        question = target.find('h1', class_='heading')
        answer = target.find('div',class_='ck-content')

        question_list = [quest.get_text() for quest in question]
        answer_list = [ans.get_text() for ans in answer]
        # Trả về danh sách các tuple (tiêu đề, ngày)
        return question_list, answer_list
    else:
        print(f"Không thể truy cập {url}. Mã lỗi: {response.status_code}")
        return []

def crawl_multiple_websites(urls):
    # Mở file CSV để ghi dữ liệu
    with open('./crawlData/beautySoup/Data_Output/camNangNguoiDung.md', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        
        # Duyệt qua các liên kết và crawl dữ liệu
        for url in urls:
            print(f"Đang crawl dữ liệu từ: {url}")
            data = crawl_website(url)
            # Ghi dữ liệu vào CSV
            for dt in data:
                writer.writerow(dt)

                
    print("Dữ liệu đã được lưu")







urls = [
    'https://www.vps.com.vn/bai-viet/kham-pha-buc-tranh-tong-quan-ve-thi-truong-chung-khoan',
    'https://www.vps.com.vn/bai-viet/vps--dong-tien-thong-minh-dau-tu-kheo-loi-nhuan-khung',
    'https://www.vps.com.vn/bai-viet/vps--tu-do-tai-chinh-la-dich-den-cua-moi-nguoi',
    'https://www.vps.com.vn/bai-viet/cpi-va-moi-lien-he-cua-no-voi-thi-truong-chung-khoan',
    'https://www.vps.com.vn/bai-viet/ai-la-ca-map-tren-thi-truong-chung-khoan-phai-sinh',
    'https://www.vps.com.vn/bai-viet/co-tuc-va-nhung-dieu-can-biet',
    'https://www.vps.com.vn/bai-viet/khi-nao-nen-chot-loi-cat-lo-hay-giu-tiep-co-phieu',
    'https://www.vps.com.vn/bai-viet/cpi-va-moi-lien-he-cua-no-voi-thi-truong-chung-khoan',
    'https://www.vps.com.vn/bai-viet/co-tuc-va-nhung-dieu-can-biet', 
    'https://www.vps.com.vn/bai-viet/vps-tim-hieu-ve-fed-to-chuc-co-kha-nang-dieu-hanh-kinh-te-toan-cau',
    'https://www.vps.com.vn/bai-viet/5-nguyen-tac-quan-tri-danh-muc-hieu-qua',
    'https://www.vps.com.vn/bai-viet/nhung-yeu-to-anh-huong-den-thi-gia-co-phieu',
    'https://www.vps.com.vn/bai-viet/tong-hop-nhung-dang-co-phieu-tren-thi-truong-khong-phai-ai-cung-biet',
    'https://www.vps.com.vn/bai-viet/checklist-nhung-viec-lam-quan-trong-khi-luong-ve',
    'https://www.vps.com.vn/bai-viet/5-dau-hieu-chi-diem-co-phieu-khong-nen-mua',
    'https://www.vps.com.vn/bai-viet/nhom-co-phieu-vn30-co-anh-huong-nhu-the-nao-den-thi-truong-chung-khoan',
    'https://www.vps.com.vn/bai-viet/vps--ven-man-sai-lam-pho-bien-khi-phan-bo-dong-tien-dau-tu',
    'https://www.vps.com.vn/bai-viet/dau-tu-theo-phuong-phap-trend-following-va-price-action',
    'https://www.vps.com.vn/bai-viet/khoi-luong-giao-dich-la-gi-va-su-dung-chi-bao-volume-the-nao-cho-hieu-qua-',
    'https://www.vps.com.vn/bai-viet/cong-cu-va-cac-chien-luoc-phan-tich-ky-thuat',
    'https://www.vps.com.vn/bai-viet/kham-pha-buc-tranh-tong-quan-ve-thi-truong-chung-khoan',
    'https://www.vps.com.vn/bai-viet/lam-phat-va-tac-dong-cua-no-len-thi-truong-chung-khoan',
    'https://www.vps.com.vn/bai-viet/cac-truong-phai-phan-tich-ky-thuat-pho-bien',
    'https://www.vps.com.vn/bai-viet/vps--cac-chi-bao-pho-bien-trong-phan-tich-ky-thuat',
    'https://www.vps.com.vn/bai-viet/phan-tich-ky-thuat-trong-dau-tu-chung-khoan-',
    'https://www.vps.com.vn/bai-viet/vang-tang-gia-nguoi-nam-giu-co-phieu-nen-lam-gi',
    'https://www.vps.com.vn/bai-viet/vps--nhung-sai-lam-can-tranh-trong-dau-tu-chung-khoan',
    'https://www.vps.com.vn/bai-viet/quyet-dinh-cua-fed-tac-dong-ra-sao-toi-thi-truong-chung-khoan-viet-nam',
    'https://www.vps.com.vn/bai-viet/vps--nghe-thuat-dau-tu-dai-han-voi-so-von-nho',
    'https://www.vps.com.vn/bai-viet/vps--dau-tu-theo-tin-don-tien-mat-tat-mang',
    'https://www.vps.com.vn/bai-viet/vps--bat-mach-tam-ly-cua-nha-dau-tu-tren-thi-truong-',
    'https://www.vps.com.vn/bai-viet/chinh-sach-tai-khoa-va-moi-lien-he-den-thi-truong-chung-khoan-viet-nam',
    'https://www.vps.com.vn/bai-viet/vps--khi-nao-nen-ban-co-phieu',
    'https://www.vps.com.vn/bai-viet/vps--cach-phong-ve-rui-ro-trong-dau-tu-chung-khoan',
    'https://www.vps.com.vn/bai-viet/vps--cac-yeu-to-then-chot-de-dau-tu-dai-han-thanh-cong-',
    'https://www.vps.com.vn/bai-viet/vps--dau-tu-theo-khau-vi-lieu-ban-co-phai-nha-dau-tu-ua-mao-hiem-',
    'https://www.vps.com.vn/bai-viet/vps--dong-tien-thong-minh-dau-tu-kheo-loi-nhuan-khung',
    'https://www.vps.com.vn/bai-viet/vps--nhung-dieu-can-biet-khi-dau-tu-co-phieu-penny',
    'https://www.vps.com.vn/bai-viet/vps--ty-gia-bien-dong-ra-sao-den-thi-truong-chung-khoan',
    'https://www.vps.com.vn/bai-viet/dau-tu-giao-dich-ngan-han-la-gi',
    'https://www.vps.com.vn/bai-viet/vps--margin-la-gi-va-nen-su-dung-margin-ra-sao-de-toi-uu-loi-nhuan',
    'https://www.vps.com.vn/bai-viet/tong-hop-cac-thuat-ngu-chung-khoan-co-ban-cho-nha-dau-tu-f0',
    'https://www.vps.com.vn/bai-viet/vps--chu-ky-nen-kinh-te-va-thi-truong-chung-khoan',
    'https://www.vps.com.vn/bai-viet/dau-tu-theo-chi-so-la-gi',
    'https://www.vps.com.vn/bai-viet/vps--tron-bo-tu-dien-ve-cac-kenh-dau-tu-cho-nguoi-moi-bat-dau',
    'https://www.vps.com.vn/bai-viet/vps--tong-quan-phan-tich-co-ban-chung-khoan-',
    'https://www.vps.com.vn/bai-viet/phuong-phap-phan-tich-co-ban-chung-khoan',
    'https://www.vps.com.vn/bai-viet/vps--cac-chi-so-chung-khoan-co-ban-nha-dau-tu-can-biet',
    'https://www.vps.com.vn/bai-viet/thuc-hanh-ap-dung-phuong-phap-phan-tich-co-ban-chung-khoan',
    'https://www.vps.com.vn/bai-viet/vps--phuong-phap-chon-loc-co-phieu-cho-nha-dau-tu-moi-',
    'https://www.vps.com.vn/bai-viet/vps--cac-nhan-to-quan-trong-trong-phan-tich-co-ban',
    'https://www.vps.com.vn/bai-viet/vps--03-tieu-chi-danh-gia-trong-phan-tich-co-ban',
    'https://www.vps.com.vn/bai-viet/vps--tu-do-tai-chinh-la-dich-den-cua-moi-nguoi',
    'https://www.vps.com.vn/bai-viet/vps--kham-pha-nhung-quy-tac-giup-tao-dung-loi-song-tai-chinh-thong-minh',
    'https://www.vps.com.vn/bai-viet/vps--giai-ma-cac-loai-hop-dong-phai-sinh',
    'https://www.vps.com.vn/bai-viet/nhung-dieu-ban-can-biet-ve-xay-dung-thap-tai-san-27032024',
    'https://www.vps.com.vn/bai-viet/vps--hieu-ro-kim-tu-do-de-huong-den-tu-do-tai-chinh-',
    'https://www.vps.com.vn/bai-viet/vps--cac-kenh-dau-tu-tai-chinh-ca-nhan-hieu-qua',
    'https://www.vps.com.vn/bai-viet/nhung-sai-lam-trong-quan-ly-tai-chinh-ca-nhan-cua-nguoi-tre-042024',
    'https://www.vps.com.vn/bai-viet/05-luu-y-khi-chinh-phuc-chung-khoan-phai-sinh',
    'https://www.vps.com.vn/bai-viet/tong-hop-cac-lenh-dieu-kien-phai-sinh-tai-vps',
    'https://www.vps.com.vn/bai-viet/bi-quyet-de-sinh-loi-hieu-qua-khi-giao-dich-chung-khoan-phai-sinh-',
    'https://www.vps.com.vn/bai-viet/vps--tong-quan-ve-chung-khoan-phai-sinh',
    'https://www.vps.com.vn/bai-viet/vps--tron-bo-tu-dien-ve-chung-khoan-phai-sinh',
    'https://www.vps.com.vn/bai-viet/nha-dau-tu-nen-lam-gi-truoc-suc-ep-tu-ty-gia',
    'https://www.vps.com.vn/bai-viet/vps---trien-vong-tu-nhom-nganh-dau-khi-trong-quy-ii2024',
    'https://www.vps.com.vn/bai-viet/co-nen-dau-tu-theo-chien-luoc-sell-in-may',
    'https://www.vps.com.vn/bai-viet/danh-sach-cac-so-dien-thoai-dang-ky-hien-thi-thuong-hieu-cua-vps',
    'https://www.vps.com.vn/bai-viet/quan-ly-thiet-bi-dang-nhap-vao-tkgd',
    'https://www.vps.com.vn/bai-viet/xac-thuc-hai-yeu-to-voi-vps-smartotp-',
    'https://www.vps.com.vn/bai-viet/vps--canh-bao-thu-doan-lua-dao-cai-dat-ung-dung-gia-mao',
    'https://www.vps.com.vn/bai-viet/vps--ngan-chan-tan-cong-social-engineering',
    'https://www.vps.com.vn/bai-viet/vps--canh-bao-ma-doc-an-minh-trong-phan-mem-gia-mao-dich-vu-cong',
    'https://www.vps.com.vn/bai-viet/vps--canh-giac-voi-lua-dao-qua-ma-qr',
    'https://www.vps.com.vn/bai-viet/canh-bao-lo-hong-imessage-tren-thiet-bi-iphone',
    'https://www.vps.com.vn/bai-viet/vps--canh-bao-hinh-thuc-lua-dao-bang-deepfake',
    'https://www.vps.com.vn/bai-viet/vps--canh-bao-thu-doan-lua-dao-cai-phan-mem-gian-diep-tren-may-tinh-dien-thoai',
    'https://www.vps.com.vn/bai-viet/vps--luu-mat-khau-tren-trinh-duyet---tien-ich-nhung-nhieu-rui-ro',
    'https://www.vps.com.vn/bai-viet/vps--khuyen-nghi-nang-cao-bao-mat-cho-mat-khau-dang-nhap'
]
crawl_multiple_websites(urls)
