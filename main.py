f = open("info.txt", 'r', encoding='utf-8')

lines = f.readlines()
values = []
for line in lines:
    values.append(line.strip().split(":")[1])

id = values[0]
pw = values[1]
pf_mail = values[2]
subject_name = values[3]
name = values[4]
school_year = values[5]
school_num = values[6]

f.close()



data1 = "교수님 안녕하십니까.\n"
data2 = "산업정보시스템전공 {}학년에 재학중인 {}학번 {}입니다.\n\n".format(school_year,school_num,name)
data3 = "학교에 입학할 때 커리큘럼을 보며 {} 과목이 꼭 수강하고 싶었던 과목이었지만 수강신청을 성공하지 못해버렸습니다.\n\n".format(subject_name)
data4 = "강의계획표를 보고도 정말 저와 맞는 방향의 수업이라고 생각했는데, 수강신청에 실패하여 못 듣기는 너무 아쉬워 교수님께 메일을 드리게 되었습니다..\n\n"
data5 = "수강신청 변경 기간에 증원의 가능성이 있는지 여쭈고 싶습니다.. 꼭 듣고 싶었던 과목이라 간절해지네요..\n"
data6 = "아니면 수업을 듣기 위해 제가 할 수 있는 일이 있는지 여쭙고 싶습니다..\n\n"
data7 = "짧은 시간이라도 내어주셔서 정말 감사합니다! 새해 복 많이 받으시기를 기원하겠습니다!"

total_data = data1 + data2 + data3 + data4 + data5+ data6 + data7



from selenium import webdriver
import time

driver = webdriver.Chrome('/Users/max53/Downloads/chromedriver')
driver.implicitly_wait(3)

driver.get('https://mail.seoultech.ac.kr/mail/login')

id_input = driver.find_element_by_id("member_id")
id_input.send_keys(id)
pw_input = driver.find_element_by_id("member_pw")
pw_input.send_keys(pw)
submit = driver.find_element_by_css_selector("[title^='로그인']")
submit.click()

mail_send_btn = driver.find_element_by_class_name("mc-btn_quick")
mail_send_btn.click()

mail_ad = driver.find_element_by_class_name("ui-autocomplete-input")
mail_ad.send_keys(pf_mail)

# driver.implicitly_wait(5)
# time.sleep(3)

subject = driver.find_element_by_id("subject")
subject.send_keys(subject_name)

driver.switch_to_frame("tx_canvas_wysiwyg") # 이번 고난의 핵심이었음!!!!!!!!!!!!!!!!!!!!!!!!! 하하하하하핳하하
body_con = driver.find_element_by_xpath("//body[@contenteditable='true']/p")
# below ----------------- tried code

# driver.execute_script("arguments[0].textContent = arguments[1];", body_con, total_data)
# WaitForElement(body_con)
# body_con = driver.find_element_by_tag_name("p")
# body_con = driver.find_element_by_tag_name("body").getAttribute("tx-content-container")
# body_con.send_keys(subject_name)
# print(body_con) /// []
body_con.send_keys(total_data)
