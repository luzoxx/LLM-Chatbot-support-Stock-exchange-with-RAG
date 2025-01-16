import requests
from bs4 import BeautifulSoup
import csv


def crawl_website(url):
    # Gửi yêu cầu HTTP tới website
    response = requests.get(url)
    
    # Kiểm tra nếu yêu cầu thành công
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        target = soup.find('div',class_='col-md-8')
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
    with open('cauHoiThuongGapMD.md', mode='w', newline='', encoding='utf-8') as file:
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
    'https://www.vps.com.vn/ca-nhan/ho-tro/cau-hoi-thuong-gap/toi-co-the-mo-nhieu-tai-khoan-chung-khoan-tai-vps-khong',
    'https://www.vps.com.vn/ca-nhan/ho-tro/cau-hoi-thuong-gap/toi-muon-uy-quyen-cho-nguoi-khac-de-thuc-hien-mo-tai-khoan-chung-khoan-thi-can-thu-tuc-gi',
    'https://www.vps.com.vn/ca-nhan/ho-tro/cau-hoi-thuong-gap/toi-da-mo-tai-khoan-truc-tuyen-tren-ung-dung-vps-smartone-vay-toi-co-phai-gui-ho-so-ban-cung-toi-vps-khong',
    'https://www.vps.com.vn/ca-nhan/ho-tro/cau-hoi-thuong-gap/toi-la-nguoi-nuoc-ngoai-va-muon-mo-tai-khoan-giao-dich-chung-khoan-thi-can-lam-nhung-thu-tuc-gi',
    'https://www.vps.com.vn/ca-nhan/ho-tro/cau-hoi-thuong-gap/de-mo-tai-khoan-tai-vps-toi-can-co-giay-to-gi',
    'https://www.vps.com.vn/ca-nhan/ho-tro/cau-hoi-thuong-gap/toi-co-the-mo-tai-khoan-giao-dich-tai-vps-qua-hinh-thuc-nao',
    'https://www.vps.com.vn/ca-nhan/ho-tro/cau-hoi-thuong-gap/toi-co-the-mo-tai-khoan-tai-vps-vao-thoi-diem-ngoai-gio-giao-dich-khong',
    'https://www.vps.com.vn/ca-nhan/ho-tro/cau-hoi-thuong-gap/toi-quet-qr-chuyen-tien-nguoi-nhan-chua-nhan-duoc-trong-khi-tai-khoan-da-tru-tien-thi-lam-nhu-the-nao-thoi-gian-xu-ly-la-bao-lau-ca-hinh-thuc-nhan-tien-vao-va-chuyen-tien-ra-khoi-tkck',
    'https://www.vps.com.vn/ca-nhan/ho-tro/cau-hoi-thuong-gap/nap-tien-vao-tai-khoan-chung-khoan-tu-tai-khoan-thanh-toan-tai-ngan-hang-tmcp-dau-tu-va-phat-trien-viet-nam-bidv-tren-ung-dung-vps-smartone-co-gioi-han-han-muc-khong',
    'https://www.vps.com.vn/ca-nhan/ho-tro/cau-hoi-thuong-gap/toi-thay-khi-tao-ma-qr-nhan-tien-tu-tkck-luon-mac-dinh-la-1-tai-khoan-chinh-toi-co-the-doi-sang-cac-tai-khoan-khac-duoc-khong',
    'https://www.vps.com.vn/ca-nhan/ho-tro/cau-hoi-thuong-gap/smartqr-la-gi-smartqr-cua-vps-co-an-toan-hay-khong',
    'https://www.vps.com.vn/ca-nhan/ho-tro/cau-hoi-thuong-gap/nop-tien-nhu-the-nao-de-tien-vao-ngay-tai-khoan-chung-khoan',
    'https://www.vps.com.vn/ca-nhan/ho-tro/cau-hoi-thuong-gap/can-lam-gi-khi-nap-tien-sai-noi-dung',
    'https://www.vps.com.vn/ca-nhan/ho-tro/cau-hoi-thuong-gap/nop-nham-tien-vao-tai-khoan-chung-khoan-cua-nguoi-khac-thi-phai-lam-the-nao',
    'https://www.vps.com.vn/ca-nhan/ho-tro/cau-hoi-thuong-gap/lam-the-nao-de-rut-tien-tu-tai-khoan-chung-khoan-tai-vps',
    'https://www.vps.com.vn/ca-nhan/ho-tro/cau-hoi-thuong-gap/toi-nop-tien-vao-tai-khoan-chung-khoan-phai-sinh-tai-vps-nhung-khong-thay-tien-tang-len',
    'https://www.vps.com.vn/ca-nhan/ho-tro/cau-hoi-thuong-gap/giao-dich-noprut-ky-quy-cua-toi-dang-xu-lybi-tu-choi-thi-phai-lam-the-nao',
    'https://www.vps.com.vn/ca-nhan/ho-tro/cau-hoi-thuong-gap/vps-dang-cung-cap-cac-hinh-thuc-chuyen-tien-nao',
    'https://www.vps.com.vn/ca-nhan/ho-tro/cau-hoi-thuong-gap/phi-nop-tien-vao-tai-khoan-chung-khoan-la-bao-nhieu',
    'https://www.vps.com.vn/ca-nhan/ho-tro/cau-hoi-thuong-gap/tai-sao-nen-su-dungchuyen-sang-su-dung-smartotp',
    'https://www.vps.com.vn/ca-nhan/ho-tro/cau-hoi-thuong-gap/toi-co-the-dung-song-song-ca-hai-phuong-thuc-nhan-otp-bang-sms-va-smartotp-khong',
    'https://www.vps.com.vn/ca-nhan/ho-tro/cau-hoi-thuong-gap/tai-sao-nhap-sai-otp-thi-he-thong-bao-tai-khoan-bi-tam-khoa',
    'https://www.vps.com.vn/ca-nhan/ho-tro/cau-hoi-thuong-gap/tai-sao-nhap-sai-ma-pin-smartopt-thi-bi-khoa-chuc-nang-smartotp',
    'https://www.vps.com.vn/ca-nhan/ho-tro/cau-hoi-thuong-gap/toi-can-phai-lam-gi-khi-mat-thiet-bi-dang-ky-smartotp',
    'https://www.vps.com.vn/ca-nhan/ho-tro/cau-hoi-thuong-gap/dung-he-dieu-hanh-nao-thi-moi-su-dung-duoc-smartotp',
    'https://www.vps.com.vn/ca-nhan/ho-tro/cau-hoi-thuong-gap/toi-co-the-dang-ky-smartotp-o-dau',
    'https://www.vps.com.vn/ca-nhan/ho-tro/cau-hoi-thuong-gap/su-dung-smartotp-co-bi-tinh-phi-khong',
    'https://www.vps.com.vn/ca-nhan/ho-tro/cau-hoi-thuong-gap/smartotp-la-gi',
    'https://www.vps.com.vn/ca-nhan/ho-tro/cau-hoi-thuong-gap/tai-sao-smartotp-co-tinh-bao-mat-cao-hon-sms-otp',
    'https://www.vps.com.vn/ca-nhan/ho-tro/cau-hoi-thuong-gap/toi-bi-mat-thiet-bi-dang-ky-smartotp-toi-can-phai-lam-gi-',
    'https://www.vps.com.vn/ca-nhan/ho-tro/cau-hoi-thuong-gap/hinh-thuc-xac-thuc-van-taykhuon-mat-la-gi',
    'https://www.vps.com.vn/ca-nhan/ho-tro/cau-hoi-thuong-gap/xac-thuc-ekyc-la-gi',
    'https://www.vps.com.vn/ca-nhan/ho-tro/cau-hoi-thuong-gap/cac-hinh-thuc-luu-ky-chung-khoan-nhu-the-nao',
    'https://www.vps.com.vn/ca-nhan/ho-tro/cau-hoi-thuong-gap/thu-tuc-luu-ky-chung-khoan-la-gi',
    'https://www.vps.com.vn/ca-nhan/ho-tro/cau-hoi-thuong-gap/huong-dan-thu-tuc-chuyen-nhuong-quyen-mua-co-phieu',
    'https://www.vps.com.vn/ca-nhan/ho-tro/cau-hoi-thuong-gap/co-the-xem-phi-giao-dich-chung-khoan-co-so-da-tra-o-dau',
    'https://www.vps.com.vn/ca-nhan/ho-tro/cau-hoi-thuong-gap/co-phieu-le-co-the-phat-sinh-khi-nao-toi-co-the-ban-co-phieu-le-bang-cach-nao',
    'https://www.vps.com.vn/ca-nhan/ho-tro/cau-hoi-thuong-gap/toi-co-the-tra-cuu-lenh-ngoai-gio-o-dau',
    'https://www.vps.com.vn/ca-nhan/ho-tro/cau-hoi-thuong-gap/uu-diem-cua-kenh-dau-tu-co-phieu-',
    'https://www.vps.com.vn/ca-nhan/ho-tro/cau-hoi-thuong-gap/so-tien-toi-thieu-can-co-de-giao-dich-co-phieu-la-bao-nhieu',
    'https://www.vps.com.vn/ca-nhan/ho-tro/cau-hoi-thuong-gap/tai-sao-toi-ban-co-phieu-ngay-hom-nay-ma-chua-rut-duoc-tien-ngay-lap-tuc',
    'https://www.vps.com.vn/ca-nhan/ho-tro/cau-hoi-thuong-gap/khi-dau-tu-co-phieu-loi-nhuan-cua-toi-toi-tu-nhung-nguon-nao',
    'https://www.vps.com.vn/ca-nhan/ho-tro/cau-hoi-thuong-gap/lenh-dieu-kien-la-gi-vps-co-nhung-loai-lenh-dieu-kien-nao-trong-giao-dich-dau-tu-co-phieu',
    'https://www.vps.com.vn/ca-nhan/ho-tro/cau-hoi-thuong-gap/toi-co-the-giao-dich-co-phieu-tai-vps-qua-nen-tang-nao',
    'https://www.vps.com.vn/ca-nhan/ho-tro/cau-hoi-thuong-gap/toi-dang-giao-dich-phai-sinh-ma-hd1m-tai-ngay-dao-han-toi-khong-dong-vi-the-cuoi-ngay-thi-hom-sau-vi-the-cua-toi-co-con-duoc-giao-dich-khong',
    'https://www.vps.com.vn/ca-nhan/ho-tro/cau-hoi-thuong-gap/toi-co-chung-khoan-tren-tai-khoan-co-so-chung-khoan-do-co-the-dung-lam-tai-san-ky-quy-de-giao-dich-phai-sinh-khong',
    'https://www.vps.com.vn/ca-nhan/ho-tro/cau-hoi-thuong-gap/tai-sao-toi-phai-ky-quy-truoc-khi-giao-dich-chung-khoan-phai-sinh',
    'https://www.vps.com.vn/ca-nhan/ho-tro/cau-hoi-thuong-gap/uu-diem-cua-kenh-dau-tu-chung-khoan-phai-sinh-',
    'https://www.vps.com.vn/ca-nhan/ho-tro/cau-hoi-thuong-gap/toi-co-the-giao-dich-chung-khoan-phai-sinh-tai-vps-qua-nen-tang-nao',
    'https://www.vps.com.vn/ca-nhan/ho-tro/cau-hoi-thuong-gap/lailo-khi-giao-dich-mot-hop-dong-chung-khoan-phai-sinh-duoc-thanh-toan-nhu-the-nao',
    'https://www.vps.com.vn/ca-nhan/ho-tro/cau-hoi-thuong-gap/khi-giao-dich-chung-khoan-phai-sinh-toi-se-phai-thanh-toan-cac-khoan-chi-phi-nao',
    'https://www.vps.com.vn/ca-nhan/ho-tro/cau-hoi-thuong-gap/vps-co-nhung-loai-lenh-dieu-kien-nao-trong-giao-dich-dau-tu-chung-khoan-phai-sinh',
    'https://www.vps.com.vn/ca-nhan/ho-tro/cau-hoi-thuong-gap/can-bao-nhieu-von-khoi-dau-de-tham-gia-cac-co-hoi-dau-tu-cung-infy',
    'https://www.vps.com.vn/ca-nhan/ho-tro/cau-hoi-thuong-gap/toi-co-the-dang-ky-nhu-cau-tiep-can-thong-tin-dau-tu-infy-vao-thoi-gian-nao',
    'https://www.vps.com.vn/ca-nhan/ho-tro/cau-hoi-thuong-gap/infy-phu-hop-voi-nha-dau-tu-nhu-the-nao',
    'https://www.vps.com.vn/ca-nhan/ho-tro/cau-hoi-thuong-gap/toi-co-the-bo-sung-tai-san-dam-bao-de-dua-tai-khoan-bi-canh-bao-ve-trang-thai-an-toan-bang-cach-nao',
    'https://www.vps.com.vn/ca-nhan/ho-tro/cau-hoi-thuong-gap/cong-ty-chung-khoan-co-the-nhan-cac-tai-san-nao-lam-tai-san-dam-bao-cho-giao-dich-ky-quy-cua-khach-hang',
    'https://www.vps.com.vn/ca-nhan/ho-tro/cau-hoi-thuong-gap/toi-co-the-hoan-tra-cac-khoan-vay-sap-toi-han-bang-cach-nao',
    'https://www.vps.com.vn/ca-nhan/ho-tro/cau-hoi-thuong-gap/cac-truong-hop-nao-se-bi-xu-ly-tai-san-dam-bao',
    'https://www.vps.com.vn/ca-nhan/ho-tro/cau-hoi-thuong-gap/giao-dich-ky-quy-la-gi',
    'https://www.vps.com.vn/ca-nhan/ho-tro/cau-hoi-thuong-gap/phi-giao-dich-khi-su-dung-san-pham-ky-quy-margin-la-bao-nhieu',
    'https://www.vps.com.vn/ca-nhan/ho-tro/cau-hoi-thuong-gap/khi-giao-dich-tren-thi-truong-co-so-ty-le-ky-quy-duoc-hieu-la-gi',
    'https://www.vps.com.vn/ca-nhan/ho-tro/cau-hoi-thuong-gap/lai-suat-vay-khi-su-dung-san-pham-ky-quy-margin-la-bao-nhieu',
    'https://www.vps.com.vn/ca-nhan/ho-tro/cau-hoi-thuong-gap/danh-muc-chung-khoan-giao-dich-ky-quy-cua-vps-bao-gom-nhung-ma-nao',
    'https://www.vps.com.vn/ca-nhan/ho-tro/cau-hoi-thuong-gap/dieu-kien-de-su-dung-san-dich-vu-giao-dich-chung-khoan-ky-quy-tai-vps-la-gi',
    'https://www.vps.com.vn/ca-nhan/ho-tro/cau-hoi-thuong-gap/toi-co-the-tra-cuu-thong-tin-ve-cac-khoan-vay-giao-dich-ky-quy-o-dau-',
    'https://www.vps.com.vn/ca-nhan/ho-tro/cau-hoi-thuong-gap/truong-hop-toi-tang-gify-nhung-nham-so-dien-thoai-nguoi-nhan-thi-phai-lam-the-nao-de-khong-bi-mat-tien',
    'https://www.vps.com.vn/ca-nhan/ho-tro/cau-hoi-thuong-gap/khi-toi-tang-qua-ma-mon-qua-het-han-hoac-toi-huy-qua-hoac-nguoi-nhan-tu-choi-qua-thi-toi-co-dc-nhan-lai-tien-da-tang-khong-toi-co-duoc-hoan-lai-phi-thiep-khong',
    'https://www.vps.com.vn/ca-nhan/ho-tro/cau-hoi-thuong-gap/can-co-dieu-kien-gi-de-su-dung-tinh-nang-gify',
    'https://www.vps.com.vn/ca-nhan/ho-tro/cau-hoi-thuong-gap/gify-la-gi',
    'https://www.vps.com.vn/ca-nhan/ho-tro/cau-hoi-thuong-gap/toi-co-the-tang-nhieu-mon-qua-cho-mot-nguoi-khong',
    'https://www.vps.com.vn/ca-nhan/ho-tro/cau-hoi-thuong-gap/gify-co-quy-dinh-so-tien-toi-thieutoi-da-khong',
    'https://www.vps.com.vn/ca-nhan/ho-tro/cau-hoi-thuong-gap/voi-san-pham-stockcard-toi-duoc-tang-nhung-ma-co-phieu-nao',
    'https://www.vps.com.vn/ca-nhan/ho-tro/cau-hoi-thuong-gap/khi-nhan-qua-stockcard-da-duoc-quy-doi-sang-co-phieu-thi-co-duoc-tinh-vao-co-phieu-co-san-cua-toi-khong',
    'https://www.vps.com.vn/ca-nhan/ho-tro/cau-hoi-thuong-gap/m-privilege-la-gi',
    'https://www.vps.com.vn/ca-nhan/ho-tro/cau-hoi-thuong-gap/m-privilege-co-uu-dai-gi',
    'https://www.vps.com.vn/ca-nhan/ho-tro/cau-hoi-thuong-gap/thuong-hieu-noi-bat-nao-dang-hop-tac-voi-m-privilege',
    'https://www.vps.com.vn/ca-nhan/ho-tro/cau-hoi-thuong-gap/thanh-vien-cua-m-privilege-gom-nhung-ai',
    'https://www.vps.com.vn/ca-nhan/ho-tro/cau-hoi-thuong-gap/cach-thuc-lien-he-hop-tac-va-tra-loi-thac-mac-cua-khach-hang',
    'https://www.vps.com.vn/ca-nhan/ho-tro/cau-hoi-thuong-gap/thiet-bi-chua-xac-thuc-la-gi',
    'https://www.vps.com.vn/ca-nhan/ho-tro/cau-hoi-thuong-gap/thiet-bi-da-xac-thuc-la-gi',
    'https://www.vps.com.vn/ca-nhan/ho-tro/cau-hoi-thuong-gap/lam-the-nao-de-battat-dang-nhap-bao-mat-2-lop',
    'https://www.vps.com.vn/ca-nhan/ho-tro/cau-hoi-thuong-gap/uu-diem-cua-bao-mat-2-lop',
    'https://www.vps.com.vn/ca-nhan/ho-tro/cau-hoi-thuong-gap/toi-can-lam-gi-de-phong-tranh-cac-hoat-dong-lua-dao',
    'https://www.vps.com.vn/ca-nhan/ho-tro/cau-hoi-thuong-gap/quan-ly-thiet-bi-la-gi',
    'https://www.vps.com.vn/ca-nhan/ho-tro/cau-hoi-thuong-gap/tinh-nang-quan-ly-thiet-bi-co-anh-huong-den-qua-trinh-giao-dich-tren-tkck-cua-toi-khi-mua-ban-co-phieu-va-su-dung-cac-san-pham-dich-vu-cua-vps-hay-khong',
    'https://www.vps.com.vn/ca-nhan/ho-tro/cau-hoi-thuong-gap/nguyen-tac-an-toan-bao-mat-tai-vps-',
    'https://www.vps.com.vn/ca-nhan/ho-tro/cau-hoi-thuong-gap/lam-the-nao-de-nang-cao-bao-mat-va-giao-dich-an-toan-tai-vps',
    'https://www.vps.com.vn/ca-nhan/ho-tro/cau-hoi-thuong-gap/khi-gap-van-de-ve-bao-mat-toi-can-lien-he-voi-vps-qua-hinh-thuc-nao',
    'https://www.vps.com.vn/ca-nhan/ho-tro/cau-hoi-thuong-gap/toi-nen-lam-gi-de-bao-ve-mat-khau-dang-nhap',
    'https://www.vps.com.vn/ca-nhan/ho-tro/cau-hoi-thuong-gap/vps-co-ap-dung-tinh-nang-dang-nhap-2-lop-hay-khong',
    'https://www.vps.com.vn/ca-nhan/ho-tro/cau-hoi-thuong-gap/vps-dang-ap-dung-chuong-trinh-uu-dai-nao-danh-cho-khach-hang-moi',
    'https://www.vps.com.vn/ca-nhan/ho-tro/cau-hoi-thuong-gap/chuong-trinh-uu-dai-lai-suat-vay-margin-tai-vps-hien-nay-la-gi',
    'https://www.vps.com.vn/ca-nhan/ho-tro/cau-hoi-thuong-gap/du-lieu-tren-chuc-nang-quan-ly-tai-san-duoc-cap-nhat-khi-nao',
    'https://www.vps.com.vn/ca-nhan/ho-tro/cau-hoi-thuong-gap/chuc-nang-quan-ly-tai-san-tren-ung-dung-vps-smartone-cung-cap-nhung-thong-tin-gi',
    'https://www.vps.com.vn/ca-nhan/ho-tro/cau-hoi-thuong-gap/dau-la-nhung-ly-do-khien-dich-vu-quan-ly-tai-san-ngay-cang-pho-bien-va-mang-den-nhieu-loi-ich-thiet-thuc',
    'https://www.vps.com.vn/ca-nhan/ho-tro/cau-hoi-thuong-gap/dich-vu-quan-ly-tai-san-la-gi',
    'https://www.vps.com.vn/ca-nhan/ho-tro/cau-hoi-thuong-gap/hien-nay-vps-dang-cung-cap-cac-san-pham-dich-vu-gi',
    'https://www.vps.com.vn/ca-nhan/ho-tro/cau-hoi-thuong-gap/chung-quyen-co-bao-dam-covered-warrant---cw-la-gi-uu-diem-cua-kenh-dau-tu-chung-quyen',
    'https://www.vps.com.vn/ca-nhan/ho-tro/cau-hoi-thuong-gap/uu-diem-cua-kenh-dau-tu-chung-quyen',
    'https://www.vps.com.vn/ca-nhan/ho-tro/cau-hoi-thuong-gap/viec-thuc-hien-chung-quyen-dien-ra-nhu-the-nao',
    'https://www.vps.com.vn/ca-nhan/ho-tro/cau-hoi-thuong-gap/chung-quyen-co-dam-bao-co-cac-loai-gia-nao',
    'https://www.vps.com.vn/ca-nhan/ho-tro/cau-hoi-thuong-gap/lam-the-nao-de-nha-dau-tu-mua-duoc-chung-quyen-co-bao-dam',
    'https://www.vps.com.vn/ca-nhan/ho-tro/cau-hoi-thuong-gap/gia-cua-chung-quyen-bi-anh-huong-boi-cac-yeu-to-nao-',
    'https://www.vps.com.vn/ca-nhan/ho-tro/cau-hoi-thuong-gap/chung-quyen-co-bao-dam-bi-huy-niem-yet-khi-nao',
    'https://www.vps.com.vn/ca-nhan/ho-tro/cau-hoi-thuong-gap/chung-chi-quy-la-gi',
    'https://www.vps.com.vn/ca-nhan/ho-tro/cau-hoi-thuong-gap/toi-nen-dau-tu-chung-chi-quy-ngan-han-hay-dai-han',
    'https://www.vps.com.vn/ca-nhan/ho-tro/cau-hoi-thuong-gap/uu-diem-cua-kenh-dau-tu-chung-chi-quy',
    'https://www.vps.com.vn/ca-nhan/ho-tro/cau-hoi-thuong-gap/quy-mo-la-gi',
    'https://www.vps.com.vn/ca-nhan/ho-tro/cau-hoi-thuong-gap/chung-chi-quy-mo-co-loi-nhuan-cao-hon-tien-gui-ngan-hang-khong',
    'https://www.vps.com.vn/ca-nhan/ho-tro/cau-hoi-thuong-gap/cac-nen-tang-giao-dich-hien-co-tai-vps',
    'https://www.vps.com.vn/ca-nhan/ho-tro/cau-hoi-thuong-gap/uu-diem-noi-bat-cua-ung-dung-vps-smartone-la-gi',
    'https://www.vps.com.vn/ca-nhan/ho-tro/cau-hoi-thuong-gap/uu-diem-noi-bat-cua-ung-dung-vps-smartpro-la-gi',
    'https://www.vps.com.vn/ca-nhan/ho-tro/cau-hoi-thuong-gap/uu-diem-noi-bat-cua-ung-dung-vps-smarteasy-la-gi',
    'https://www.vps.com.vn/ca-nhan/ho-tro/cau-hoi-thuong-gap/toi-da-mo-tai-khoan-chung-khoan-tai-vps-qua-website-openaccountvpscomvn-thi-co-the-dang-nhap-vao-cac-nen-tang-giao-dich-cua-vps-duoc-hay-khong',
    'https://www.vps.com.vn/ca-nhan/ho-tro/cau-hoi-thuong-gap/loi-nhuan-toi-se-nhan-duoc-khi-dau-tu-cung-fnest-la-gi',
    'https://www.vps.com.vn/ca-nhan/ho-tro/cau-hoi-thuong-gap/dau-tu-cung-fnest-co-diem-gi-khac-biet',
    'https://www.vps.com.vn/ca-nhan/ho-tro/cau-hoi-thuong-gap/lam-the-nao-de-dau-tu-cung-fnest',
    'https://www.vps.com.vn/ca-nhan/ho-tro/cau-hoi-thuong-gap/dau-tu-fnest-tren-ung-dung-vps-smartone-co-uu-diem-gi',
    'https://www.vps.com.vn/ca-nhan/ho-tro/cau-hoi-thuong-gap/toi-can-bo-ra-so-von-bao-nhieu-de-co-the-mua-fnest',
    'https://www.vps.com.vn/ca-nhan/ho-tro/cau-hoi-thuong-gap/toi-co-the-truy-cap-chuc-nang-quan-ly-tai-san-o-dau-tren-ung-dung-vps-smartone'
]
crawl_multiple_websites(urls)
