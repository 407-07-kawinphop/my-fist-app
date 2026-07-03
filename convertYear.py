import streamlit as st
st.title("แอปพลิเคชั่นแปลงปี พ.ศ. เป็น ค.ศ.")

bh_year=st.number_input("กรอกปี พ.ศ. ที่ต้องการแปลง",value=2569)
ce_year=bh_input-543
st.header("ปี พ.ศ. คือ: ce_year}")
