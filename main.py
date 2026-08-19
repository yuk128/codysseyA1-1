import json
import time

# 메모
# 상세 보기 만들기(수정 삭제 기능포함)
# 

def load_data():
    try:
        f = open("prompts.json", "r", encoding="utf-8")
        data = json.load(f)
        f.close()
        return data["categorys"], data["prompts"]
    except FileNotFoundError:
        categorys = ["텍스트 생성", "이미지 생성", "자동화"]
        prompts = [{
                "id": 1,
                "title": "SEO 블로그 글 작성",
                "content": "주어진 주제로 SEO에 최적화된 블로그 글을 작성해줘.",
                "category": categorys[0],
                "favorite": True
            },{
                "id": 2,
                "title": "비즈니스 영문 이메일 번역",
                "content": "다음 내용을 정중한 톤의 비즈니스 영문 이메일로 바꿔줘.",
                "category": categorys[0],
                "favorite": False
            },{
                "id": 3,
                "title": "3D 스마트워치 썸네일",
                "content": "파스텔톤 배경의 세련된 3D 스마트워치 렌더링 이미지 생성해줘.",
                "category": categorys[1],
                "favorite": True
            },{
                "id": 4,
                "title": "카페 인테리어 컨셉샷",
                "content": "따뜻한 햇살이 들어오는 우드톤 앤티크 카페 인테리어 사진.",
                "category": categorys[1],
                "favorite": False
            },{
                "id": 5,
                "title": "뉴스 기사 3줄 요약",
                "content": "제공된 뉴스 기사의 핵심 내용을 3줄로 요약해줘.",
                "category": categorys[2],
                "favorite": True
            },{
                "id": 6,
                "title": "주간 업무 보고서 정리",
                "content": "작업 내역을 성과, 계획, 리스크 3가지 파트로 정돈해줘.",
                "category": categorys[2],
                "favorite": False
            }
        ]
        return categorys, prompts

def save_data():
    f = open("prompts.json", "w", encoding="utf-8")
    json.dump({"categorys": categorys, "prompts": prompts}, f, ensure_ascii=False, indent=2)
    f.close()

categorys, prompts = load_data()

def start_print():
    print("="*10,"프롬포트 정리 프로그램","="*10)
    print("사용하실 기능을 선택해 주세요")
    print("1. 프롬프트 추가")
    print("2. 목록 보기")
    print("3. 카테고리별 조회")
    print("4. 검색")
    print("5. 즐겨찾기")
    print("6. 상세보기")
    print("7. 내보내기")
    answer = input()
    return answer

def diteil_print():
    print("="*10)
    print("사용하실 기능을 선택해 주세요")
    print("1. 수정")
    print("2. 삭제")
    print("3. 즐겨찾기 추가/해제")
    print("4. 뒤로가기")
    answer = input()
    return answer


def list_check(list, string):
    for i in range(len(list)):
        if string==list[i]:
            return True, i

    return False, len(list)



while True:
    stringvalue = start_print()
    if stringvalue == "1":
        print("프롬포트 추가")
        title = input("제목: ")
        while title == "":
            title = input("제목: ")

        content = input("프롬포트: ")
        while content == "":
            content = input("프롬포트: ")

        category = input("카테고리: ")
        while category == "":
            category = input("카테고리: ")

        a,b = list_check(categorys,category)

        if not a:
            categorys.append(category)
            
        categA = categorys[b]

        newid = len(prompts) + 1

        prompts.append({"id": newid,
                "title": title,
                "content": content,
                "category": categA,
                "favorite": False})

        
    elif stringvalue == "2":
        print("전체 프롬포트 목록")
        for i in range(len(prompts)):
            if prompts[i]["favorite"]:
                star = "⭐"
            else:
                star = ""
            print(f"{prompts[i]["id"]}. {prompts[i]["title"]}{star} {prompts[i]["category"]}")
            
    elif stringvalue == "3":
        print(categorys)
        numA = input("카테고리 번호")
        c=numA.isdigit()

        if c:
            numB = int(numA)
            if numB < len(categorys):
                for i in prompts:
                    if i["category"] == categorys[int(numB-1)]:
                        print(f"{i["title"]} ({i["id"]})")

    elif stringvalue == "4":
        print("프롬포트 검색")
        keyword = input("검색어: ")
        count = 0

        for i in range(len(prompts)):
            if keyword in prompts[i]["title"] or keyword in prompts[i]["content"]:
                print(f"{prompts[i]["title"]} ({prompts[i]["id"]})")
                count = count + 1

        if count == 0:
            print("검색 결과가 없습니다.")
        else:
            print(f"{count}개의 프롬프트를 찾았습니다.")


       
    elif stringvalue == "5":
        for i in prompts:
            if i["favorite"]:
                print(f"{i["title"]} ({i["id"]})")


    elif stringvalue == "6":
        numC = input("프롬포트 번호: ")
        
        d = numC.isdigit()

        if d:
            numD = int(numC)
            found = False

            for i in prompts:
                if i["id"] == numD:
                    found = True
                    print(f"제목: {i["title"]}")
                    print(f"카테고리: {i["category"]}")
                    if i["favorite"]:
                        print("즐겨찾기: O")
                    else:
                        print("즐겨찾기: X")
                    print(f"내용: {i["content"]}")
                    input()

                    numE = diteil_print()
                    if numE == "1":
                        print("프롬포트 수정")
                        newtitle = input("새 제목: ")
                        newcontent = input("새 내용: ")
                        newcategory = input("새 카테고리: ")
                        a,b = list_check(categorys, newcategory)

                        if not a:
                            categorys.append(newcategory)
                        catB = categorys[b]

                        i["title"] = newtitle
                        i["content"] = newcontent
                        i["category"] = catB
                        print("수정 되었습니다.")

                    elif numE == "2":
                        prompts.remove(i)
                        print("삭제 되었습니다.")
                        break

                    elif numE == "3":
                        if i["favorite"]:
                            i["favorite"] = False
                            print("즐겨찾기가 해제되었습니다.")
                        else:
                            i["favorite"] = True
                            print("즐겨찾기에 추가되었습니다.")

                    elif numE == "4":
                        print("시작 메뉴로 이동합니다.")

                    else:
                        print("잘못된 형식 입니다.")
                    

            if not found:
                print("해당 번호의 프롬프트가 없습니다.")
        else:
            print("숫자를 입력해주세요.")

    elif stringvalue == "7":
        f = open("prompts.md", "w", encoding="utf-8")

        for cat in categorys:
            f.write(f"## {cat}\n")
            for i in prompts:
                if i["category"] == cat:
                    f.write(f"- {i["title"]} ({i["id"]})\n {i["content"]} \n")
            f.write("\n")

        f.close()
        print("prompts.md 파일로 내보냈습니다.")


    elif stringvalue == "q":
        save_data()
        break
    else:
        print("잘못된 형식 입니다.")
        print(f"입력된 값: {stringvalue}")
    save_data()
    input()

print("프로그램이 종료 되었습니다.")