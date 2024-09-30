import streamlit as st

# 질문 리스트
questions = [
    {"question": "어떤 유형의 프로젝트를 진행하시나요?", 
     "options": ["웹 애플리케이션", "모바일 애플리케이션", "데이터 분석", "AI 모델"]},
    {"question": "어떤 언어로 개발하시겠습니까?", 
     "options": ["Python", "JavaScript", "Java", "C++"]},
    {"question": "사용할 프레임워크나 라이브러리는 무엇입니까?", 
     "options": ["Django", "Flask", "React", "TensorFlow"]},
]

# 응답 저장 리스트
responses = []

st.title("Prompt Engineering Bot")

# 질문을 순서대로 출력하고 사용자의 응답을 저장
for i, q in enumerate(questions):
    st.write(f"Q{i+1}: {q['question']}")
    response = st.radio("", q["options"], key=f"q{i}")
    responses.append(response)
    st.write("---")

# 사용자의 응답을 기반으로 최종 프롬프트 생성
if st.button("결과 생성"):
    prompt = f"당신은 {responses[0]} 프로젝트를 진행하고 있으며, 주 언어는 {responses[1]}입니다. 프레임워크로는 {responses[2]}을(를) 사용합니다."
    
    # LLM의 역할을 정의하는 프롬프트
    st.write("### 생성된 프롬프트:")
    st.write(prompt)

    # 추후 이 프롬프트를 LLM에 넘길 수 있도록 설정 가능
