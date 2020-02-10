school_year = input("학년을 입력하세요:(2 => O, 2학년 => X)")
school_num = input("학번을 입력하세요: (19 => O, 19학번 => X)")
name = input("이름을 입력하세요:")
subject = input("과목이름을 입력하세요")

f = open('C:/Users/max53/OneDrive/바탕 화면/mail.txt', 'w', encoding='utf-8')

data1 = "교수님 안녕하십니까.\n"
data2 = "산업정보시스템전공 {}학년에 재학중인 {}학번 {}입니다.\n\n".format(school_year,school_num,name)
data3 = "학교에 입학할 때 커리큘럼을 보며 {} 과목이 꼭 수강하고 싶었던 과목이었지만 수강신청을 성공하지 못해버렸습니다.\n\n".format(subject)
data4 = "강의계획표를 보고도 정말 저와 맞는 방향의 수업이라고 생각했는데, 수강신청에 실패하여 못 듣기는 너무 아쉬워 교수님께 메일을 드리게 되었습니다..\n\n"
data5 = "수강신청 변경 기간에 증원의 가능성이 있는지 여쭈고 싶습니다.. 꼭 듣고 싶었던 과목이라 간절해지네요..\n"
data6 = "아니면 수업을 듣기 위해 제가 할 수 있는 일이 있는지 여쭙고 싶습니다..\n\n"
data7 = "짧은 시간이라도 내어주셔서 정말 감사합니다! 새해 복 많이 받으시기를 기원하겠습니다!"
f.write(data1)
f.write(data2)
f.write(data3)
f.write(data4)
f.write(data5)
f.write(data6)
f.write(data7)

f.close()
