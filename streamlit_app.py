import streamlit as st
from datetime import date

# 질문 리스트
questions = [
    {"question": "어떤 유형의 문서를 찾고 계십니까?", 
     "options": ["회의록", "보고서", "계약서", "마케팅 자료", "기획서", "기타"]},
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

# 세션 상태에서 날짜 값을 관리
if 'start_date' not in st.session_state:
    st.session_state['start_date'] = date.today()

if 'end_date' not in st.session_state:
    st.session_state['end_date'] = date.today()

# 질문을 순서대로 출력하고 사용자의 응답을 저장
for i, q in enumerate(questions):
    st.write(f"Q{i+1}: {q['question']}")
    # 가로로 라디오 버튼 배치 (horizontal)
    response = st.radio("", q["options"], key=f"q{i}", horizontal=True)
    
    # '특정 날짜' 선택 시 날짜 입력 필드 표시
    if i == 1 and response == "특정 날짜":
        start_date = st.date_input("시작 날짜를 선택하세요", value=st.session_state['start_date'], key=f"start_date_{i}")
        end_date = st.date_input("종료 날짜를 선택하세요", value=st.session_state['end_date'], key=f"end_date_{i}")
        
        # 시작 날짜가 종료 날짜보다 이후일 경우
        if start_date > end_date:
            st.warning("종료 날짜가 시작 날짜보다 이전일 수 없습니다. 종료 날짜가 시작 날짜로 변경됩니다.")
            st.session_state['end_date'] = start_date  # 종료 날짜를 시작 날짜로 변경

        # 세션 상태에 날짜 업데이트
        st.session_state['start_date'] = start_date
        st.session_state['end_date'] = end_date
        
        response = f"{st.session_state['start_date'].strftime('%Y-%m-%d')} ~ {st.session_state['end_date'].strftime('%Y-%m-%d')}"  # 날짜 범위를 문자열로 변환
    
        # 시작 날짜와 종료 날짜가 같다면 기간 제외
        if st.session_state['start_date'] == st.session_state['end_date']:
            response = f"{st.session_state['start_date'].strftime('%Y-%m-%d')}"  # 날짜를 문자열로 변환

    # '기타' 선택 시 텍스트 입력 필드 표시
    if (i == 0 or i == 3) and response == "기타":
        other_input = st.text_input("세부 내용을 입력하세요", key=f"other_{i}")
        response = other_input
    
    responses.append(response)
    st.write("---")

# 사용자의 응답을 기반으로 최종 프롬프트 생성
if st.button("결과 생성"):
    prompt = f"{responses[2]}에서 {responses[1]} 동안 작성된 {responses[3]} {responses[0]}를(을) {responses[4]} 형식으로 찾고 있습니다. 이 문서는 {responses[5]}를 위해 사용될 것입니다."
    
    # 생성된 프롬프트를 코드블록으로 표시
    st.write("### 생성된 프롬프트:")
    st.code(prompt, language='text', wrap_lines = True)

    # 복사 버튼과 JavaScript를 이용한 복사 기능 구현
    # st.markdown(f"""
    # <button onclick="copyToClipboard()">복사</button>
    # <script>
    # function copyToClipboard() {{
    #     const text = `{prompt}`;
    #     navigator.clipboard.writeText(text).then(function() {{
    #         alert('프롬프트가 클립보드에 복사되었습니다!');
    #     }}, function(err) {{
    #         alert('복사 실패: ' + err);
    #     }});
    # }}
    # </script>
    # """, unsafe_allow_html=True)
