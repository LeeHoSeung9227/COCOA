# OSU Debris Detection Project

이 프로젝트는 YOLOv8을 사용하여 해양 쓰레기(debris)를 탐지하고 추적하는 시스템입니다.

## 프로젝트 개요

- **목적**: 해양 환경에서의 쓰레기 탐지 및 추적
- **모델**: YOLOv8 (Ultralytics)
- **데이터셋**: Roboflow에서 제공하는 block-irbax 데이터셋
- **클래스 수**: 16개 클래스 (Hand, blue_cube, blue_longrect, blue_rect, cylinder, green_cube, green_longrect, green_rect, half_cylinder, red_cube, red_rect, triangle, yellow_archrect, yellow_cube, yellow_longrect, yelow_rect)

## 파일 구조

```
OSU_Debris/
├── data.yaml              # 데이터셋 설정 파일
├── yolov8.py             # 메인 실행 파일
├── yolov8n.pt           # YOLOv8 모델 파일
├── train/               # 훈련 데이터
│   ├── images/          # 훈련 이미지
│   └── labels/          # 훈련 라벨
├── valid/               # 검증 데이터
│   ├── images/          # 검증 이미지
│   └── labels/          # 검증 라벨
├── test/                # 테스트 데이터
│   ├── images/          # 테스트 이미지
│   └── labels/          # 테스트 라벨
└── runs/                # 실행 결과
    └── debris_video.mp4 # 테스트 비디오
```

## 사용법

1. 필요한 패키지 설치:
```bash
pip install ultralytics
```

2. 모델 실행:
```bash
python yolov8.py
```

## 설정

- **Confidence threshold**: 0.3
- **IoU threshold**: 0.50
- **Tracker**: ByteTrack
- **Device**: CPU (GPU 사용 시 'cuda'로 변경)

## 데이터셋 정보

- **출처**: [Roboflow Universe - block-irbax](https://universe.roboflow.com/terabaru/block-irbax/dataset/5)
- **라이선스**: CC BY 4.0
- **버전**: 5

## 라이선스

이 프로젝트는 CC BY 4.0 라이선스 하에 있습니다.
