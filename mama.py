import streamlit as st

st.title("Welcome to Mama channel")
st.header("hello guys i am back with another program")
st.subheader("In this a will be tell you how to make program in python")
st.markdown("First you want to open python then open command prompt then type pip install streamlit then enter then make program and again command prompt then type streamlit run your python file name.py then enter then you get the local host address")
st.code("""st.title("Welcome to Mama channel")
st.header("hello guys i am back with another program")
st.subheader("In this a will be tell you how to make program in python")
st.markdown("First you want to open python then open command prompt then type pip install streamlit then enter then make program and again command prompt then type streamlit run your python file name.py then enter then you get the local host address")  
        """)


name = st.text_input("Enter Your Name : ")
Fname = st.text_input("Enter Your Father Name : ")
adr = st.text_area("Enter Your Adress : ")
classdata = st.selectbox("Enter Your Class :",(1,2,3,4,5,6,7,8,9,10))

button = st.button("Done")
if button :
    st.markdown(f"""
    Name : {name}
    Father Name : {Fname}
    Adress :{adr}
    class : {classdata}""")





                

