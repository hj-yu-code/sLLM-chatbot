import streamlit as st

# 질문 리스트
questions = [
    {"question": "어떤 유형의 문서를 찾고 계십니까?", 
     "options": ["회의록", "보고서", "계약서", "마케팅 자료", "기획서"]},
    {"question": "어느 기간의 자료를 찾으시나요?", 
     "options": ["지난 1개월", "지난 6개월", "지난 1년", "특정 날짜"]},
    {"question": "어느 부서의 자료를 찾으십니까?", 
     "options": ["총무팀", "마케팅팀", "기획팀", "인사팀", "재무팀"]},
    {"question": "찾고 있는 문서의 주요 내용은 무엇입니까?", 
     "options": ["예산 관련", "프로젝트 진행 상황", "고객 관련 정보", "마케팅 전략", "기타"]},
    {"question": "어떤 형식의 문서를 찾으십니까?", 
     "options": ["PDF", "Excel", "Word", "PowerPoint", "텍스트 파일"]},
    {"question": "문서를 어떤 목적으로 사용하시나요?", 
     "options": ["참고용", "보고서 작성", "발표 준비", "분석 작업", "협업"]}
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
    # "마케팅팀에서 지난 1년 동안 작성된 예산 관련 보고서를 PDF 형식으로 찾고 있습니다. 이 문서는 발표 준비를 위해 사용될 것입니다."
    prompt = f"{responses[2]}에서 {responses[1]} 동안 작성된 {responses[3]} {responses[0]}를(을) {responses[4]} 형식으로 찾고 있습니다. 이 문서는 {responses[5]}를 위해 사용될 것입니다."
    
    # LLM의 역할을 정의하는 프롬프트
    st.write("### 생성된 프롬프트:")
    st.write(prompt)

    # 추후 이 프롬프트를 LLM에 넘길 수 있도록 설정 가능
