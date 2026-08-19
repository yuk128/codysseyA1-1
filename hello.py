import json

prompts = [{
        "title": "SEO 블로그 글 작성",
        "content": "주어진 주제로 SEO에 최적화된 블로그 글을 작성해줘.",
        "category": "텍스트 생성",
        "favorite": True
    },{
        "title": "비즈니스 영문 이메일 번역",
        "content": "다음 내용을 정중한 톤의 비즈니스 영문 이메일로 바꿔줘.",
        "category": "텍스트 생성",
        "favorite": False
    },{
        "title": "3D 스마트워치 썸네일",
        "content": "파스텔톤 배경의 세련된 3D 스마트워치 렌더링 이미지 생성해줘.",
        "category": "이미지 생성",
        "favorite": True
    },{
        "title": "카페 인테리어 컨셉샷",
        "content": "따뜻한 햇살이 들어오는 우드톤 앤티크 카페 인테리어 사진.",
        "category": "이미지 생성",
        "favorite": False
    },{
        "title": "뉴스 기사 3줄 요약",
        "content": "제공된 뉴스 기사의 핵심 내용을 3줄로 요약해줘.",
        "category": "자동화",
        "favorite": True
    },{
        "title": "주간 업무 보고서 정리",
        "content": "작업 내역을 성과, 계획, 리스크 3가지 파트로 정돈해줘.",
        "category": "자동화",
        "favorite": False
    }
]

def start_print():
    print("사용하실 기능을 선택해 주세요")
    print("1. 프롬프트 추가")
    print("2. 목록 보기")
    print("3. 카테고리별 조회")
    print("4. 검색")
    print("5. 상세 보기")
    print("6. 즐겨찾기")
    answer = input()
    return answer


stringvalue = start_print()

if stringvalue == "1":
    print("전체 프롬포트 목록")
    for i in range(len(prompts)):
        print(f"{i+1}. {prompts[i]["title"]}")
else:
    print("잘못된 형식 입니다.")
    print(f"입력된 값: {stringvalue}")


print("프로그램이 종료 되었습니다.")