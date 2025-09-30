from ultralytics import YOLO
# 1. 모델 로드 (custom.pt)
model = YOLO('yolov8n.pt')
# 2. Tracking 실행
results = model.track(
    source=r'C:\Users\COEL_03\Desktop\OSU_Debris\runs\debris_video.mp4', # 영상 경로 (혹은 0 -> 웹캠)
    tracker='bytetrack.yaml', # 추적기 설정 (YOLOv8 내장)
    conf=0.3, # confidence threshold
    iou=0.50, # IoU threshold
    show=True, # 화면에 실시간 표시
    save=True, # 결과 저장
    device='cpu' # GPU 없으면 'cpu'
)