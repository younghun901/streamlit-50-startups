# 스타트업 수익 예측 앱

간단한 Streamlit 웹앱으로, 50개 스타트업 데이터셋을 기반으로 연간 수익(Profit)을 예측합니다.

## 주요 기능
- Home: 프로젝트 및 데이터셋 소개(앱의 메인 타이틀 아래에 표시)
- EDA: 탐색적 데이터 분석 공간(현재 자리 보존)
- ML: 사용자 입력으로 수익 예측(모델 로드 후 예측)

## 요구사항
- Python 3.8+
- 의존 패키지: requirements.txt 참조

예시(프로젝트 루트에서):
```bash
pip install -r requirements.txt
```

requirements.txt에 포함된 주요 패키지:
- streamlit
- pandas
- numpy
- joblib
- scikit-learn

## 설치 및 실행
프로젝트 루트(/Users/younghun/Documents/GitHub/streamlit-50-startups)에서:
```bash
pip install -r requirements.txt
streamlit run app.py
```

브라우저에서 표시되는 로컬 URL로 접속하여 사용.

## 모델 파일
예측은 저장된 파이프라인 파일(`./model/pipe.pkl`)을 사용합니다. 해당 파일이 없으면 예측이 실패합니다.
- 모델이 없는 경우: 노트북(`데이터분석_머신러닝.ipynb`)에서 학습 후 `joblib.dump(pipe, './model/pipe.pkl')`로 저장하세요.

## 입력값(ML 메뉴)
- R&D Spend (연구개발비) — 숫자 입력
- Administration (운영비) — 숫자 입력
- Marketing Spend (마케팅비) — 숫자 입력
- State (지역) — California / Florida / New York 중 선택

예측 버튼을 누르면 예상 수익(달러)을 출력합니다.

## 프로젝트 구조(주요 파일)
- app.py — Streamlit 앱 진입점(메뉴 및 홈 마크다운 표시)
- app_ML.py — ML 관련 UI 및 예측 로직
- model/pipe.pkl — 저장된 예측 파이프라인 (필요)
- data/50_Startups.csv — 원본 데이터(참고용)
- 데이터분석_머신러닝.ipynb — 데이터 분석 및 모델 학습 노트북
- requirements.txt — 의존성 목록

## 참고
- Home 선택 시 프로젝트 소개/데이터셋 정보가 표시됩니다. ML 메뉴에서는 소개 마크다운이 표시되지 않도록 구성되어 있습니다.
