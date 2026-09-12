import time
import streamlit as st

st.title("⏰ เกมเติมศัพท์จับเวลา")

if "ans1_val" not in st.session_state:
    st.session_state.ans1_val = ""
if "ans2_val" not in st.session_state:
    st.session_state.ans2_val = ""
if "ans3_val" not in st.session_state:
    st.session_state.ans3_val = ""
if "ans4_val" not in st.session_state:
    st.session_state.ans4_val = ""
if "ans5_val" not in st.session_state:
    st.session_state.ans5_val = ""

def reset_game():
    st.session_state.ans1_val = "" # เคลียร์ค่าช่องข้อ 1
    st.session_state.ans2_val = "" # เคลียร์ค่าช่องข้อ 2
    st.session_state.ans3_val = "" # เคลียร์ค่าช่องข้อ 3
    st.session_state.ans4_val = "" # เคลียร์ค่าช่องข้อ 4
    st.session_state.ans5_val = "" # เคลียร์ค่าช่องข้อ 5
    st.session_state.start = time.time() # เริ่มเวลาใหม่
    st.session_state.is_ended = False # ปิด Dialog
  

@st.dialog("📊 สรุปผลการเล่นเกม")
def show_result_dialog(ans1, ans2, ans3, ans4, ans5):
    st.balloons()
    score = 0

    u_ans1 = ans1.strip().lower()
    u_ans2 = ans2.strip().lower()
    u_ans3 = ans3.strip().lower()
    u_ans4 = ans4.strip().lower()
    u_ans5 = ans5.strip().lower() 
  
    if u_ans1 == "me too - 3.2.1":
        st.success("✅ ข้อ 1: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 1: ยังไม่ถูกต้อง (คุณตอบ '{u_ans1}')")

  
    if u_ans2 == "ดึงดัน - ค็อกเทล":
        st.success("✅ ข้อ 2: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 2: ยังไม่ถูกต้อง (คุณตอบ '{u_ans2}')")

  
    if u_ans3 == "ใจบาง - Lummun":
        st.success("✅ ข้อ 3: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 3: ยังไม่ถูกต้อง (คุณตอบ '{u_ans3}')")


    if u_ans4 == "มักอ้ายหลายเด้อ - กวาง จิรพรรณ":
        st.success("✅ ข้อ 4: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 4: ยังไม่ถูกต้อง (คุณตอบ '{u_ans4}')")


    if u_ans5 == "ฟ้า - Tattoo colour":
        st.success("✅ ข้อ 5: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 5: ยังไม่ถูกต้อง (คุณตอบ '{u_ans5}')")

    st.info(f"🏅 ได้คะแนนรวม: {score} คะแนน")

    if score == 5:
      st.success("🎉 คุณผ่านแล้วเก่งมาก ")  
    elif 1 <= score <= 4:
      st. warning ("คุณเกือบผ่านแล้วฟังบ่อยๆนะ")
    else:
      st.error ("คุณแพ้ ลองฟังเพลงที่หลากหลายและเยอะขึ้นนะ")


st.button(" เริ่มเล่นเกม", on_click=reset_game)

if "start" in st.session_state and not st.session_state.get("is_ended", False):
    time_left = int(60 - (time.time() - st.session_state.start))

    if time_left > 0:
        st.error(f"⏳ เหลือเวลา: {time_left} วินาที")
    else:
        st.session_state.is_ended = True
        st.rerun()

st.divider()


ans1 = st.text_input(
     "ข้อ 1: อะ..อ้าว เธอรู้ตัวบ้างไหม ใครเขาคอยใส่ใจ",
     value=st.session_state.ans1_val,
)
ans2 = st.text_input(
     "ข้อ 2: โอ้ใจเอ๋ย ทำไมหัวใจไม่หลาบจำ ดึงดันยังรักเทออยู่ ",
     value=st.session_state.ans2_val,
)

st.session_state.ans1_val = ans1
st.session_state.ans2_val = ans2

ans3 = st.text_input(
     "ข้อ 3: เชิญครับคุณผู้หญิง อิงซบตามสบาย ",
     value=st.session_state.ans3_val,
)
ans4 = st.text_input(
     "ข้อ 4: น้องเหลียวเบิ่งทางซ้าย แล้วหันมาแนมขวา อ้ายขยิบตาแล้วยิ้มมา หัวใจเต้น ",
     value=st.session_state.ans4_val,
)
ans5 = st.text_input(
     "ข้อ 5: ฟ้าถ้าไม่ส่งมา ให้เทอมีใจ  ",
     value=st.session_state.ans5_val,
)

st.session_state.ans3_val = ans3
st.session_state.ans4_val = ans4
st.session_state.ans5_val = ans5


if "start" in st.session_state and not st.session_state.get("is_ended", False):
    if st.button("ส่งคำตอบ"):
        st.session_state.is_ended = True
        st.rerun()

    time.sleep(1)
    st.rerun()


if st.session_state.get("is_ended", False):
    show_result_dialog(ans1, ans2, ans3, ans4, ans5)

st.divider()
st.write("นายกวินภพ กันทนาวินนท์ เลขที่ 7 ม.4/7")


