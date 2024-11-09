import cv2

# 카메라를 통해 QR 코드를 스캔하는 함수
def scan_qr_code():
    # 카메라 열기
    cap = cv2.VideoCapture(0)
    
    detector = cv2.QRCodeDetector()

    while True:
        # 프레임 읽기
        _, img = cap.read()
        
        # QR 코드 데이터와 위치를 추출
        data, bbox, _ = detector.detectAndDecode(img)
        
        if data:
            print("QR 코드에 담긴 데이터:", data)
            break
        
        # 화면에 카메라 영상 표시
        cv2.imshow("QR Code Scanner", img)
        
        # 'q' 키를 누르면 스캔 종료
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    # 카메라 릴리스 및 창 닫기
    cap.release()
    cv2.destroyAllWindows()
    
    return data

# QR 코드 스캔 함수 호출
qr_data = scan_qr_code()
print("QR 코드에서 추출한 데이터:", qr_data)
