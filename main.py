import qrcode

# QR 코드에 담을 데이터 설정
data = "https://wandoo.neocities.org/"

# QR 코드 생성 및 설정
qr = qrcode.QRCode(
    version=1,  # QR 코드의 버전 (1이 가장 기본)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # 오류 수정 능력
    box_size=10,  # QR 코드 박스 크기
    border=4,     # 테두리 여백 크기
)
qr.add_data(data)
qr.make(fit=True)

# QR 코드 이미지 만들기
img = qr.make_image(fill="black", back_color="white")
img.save("wandooQR.png")  # 이미지 파일로 저장

'''
# 예시 데이터: 상대방 기기 정보 URL 또는 텍스트
data = "https://example.com/device_info"  # 기기 정보가 담긴 URL 또는 문자열
qr = qrcode.make(data)

# QR 코드를 이미지 파일로 저장
qr.save("device_info_qr.png")
print("QR 코드가 생성되었습니다: device_info_qr.png")
'''
