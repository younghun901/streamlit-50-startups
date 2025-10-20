import streamlit as st

from app_ML import run_ML

def main():
    st.title('스타트업 수익 예측 앱')

    st.subheader('스타트업 수익 예측 프로젝트')

    menu = ['Home', 'EDA', 'ML']
    choice = st.sidebar.selectbox('메뉴', menu)

    if choice in ['Home']:
        st.markdown("""
        **프로젝트 소개**
        - 목표: 50개 스타트업 데이터로부터 연간 수익(Profit)을 예측합니다.
        - 주요 기능: 탐색적 데이터 분석(EDA) 및 머신러닝 기반 예측(모델 학습/평가/예측)

        **데이터셋 정보**
        - 데이터셋: '50 Startups' (총 50개 샘플)
        - 주요 변수:
          - R&D Spend: 연구개발 비용
          - Administration: 관리비
          - Marketing Spend: 마케팅 비용
          - State: 지역(카테고리)
          - Profit: 목표 변수(수익)
        - 출처: 공개 교육용 데이터셋(예: Kaggle/UCI 등)
        """)

    if choice == menu[0]:
        pass
    elif choice == menu[1]:
        pass
    elif choice == menu[2]:
        run_ML()





if __name__ == '__main__':
    main()