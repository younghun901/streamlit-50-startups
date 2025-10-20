import streamlit as st

from app_ML import run_ML

def main():
    st.title('스타트업 수익 예측 앱')

    menu = ['Home', 'EDA', 'ML']
    choice = st.sidebar.selectbox('메뉴', menu)
    if choice == menu[0]:
        pass
    elif choice == menu[1]:
        pass
    elif choice == menu[2]:
        run_ML()





if __name__ == '__main__':
    main()