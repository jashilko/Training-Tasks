def cleanPhone(phone):
    phone =  phone.replace(")", "").replace("(", "").replace("-", "").replace("+7", "")
    if len(phone) == 7:
        phone = "495"+ phone
    if len(phone) == 11:
        phone = phone[1:]

    return phone

phone_new = cleanPhone(input())
phone1 = cleanPhone(input())
phone2 = cleanPhone(input())
phone3 = cleanPhone(input())

for ph in [phone1, phone2, phone3]:
    print("YES" if phone_new == ph else "NO")