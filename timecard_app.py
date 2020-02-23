import ezsheets
import requests
from bs4 import BeautifulSoup

workdate_list = []
names = []
session_lengths = []

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36"
}

login_data = {
    "username": "",
    "password": "",

}

date = input("Paste URL of paystub sheet:  ")
spread = ezsheets.Spreadsheet(date)
#change? url encode?

cont = input("Enter a work date? Y/N  ")
while cont == "Y":
    schedule_date = str(input("Which date (yyyy-mm-dd)? "))
    workdate_list.append(schedule_date)
    payload = {
        "minDate": schedule_date,
        "maxDate": schedule_date,
        "calendarID": "395910"

    }
    for item in workdate_list:
        req = requests.get("https://acuityscheduling.com/api/v1/appointments", params=payload, auth=(login_data["username"], login_data["password"]))
        schedule_soup = BeautifulSoup(req.content, "html5lib")
        print(schedule_soup)
        #decode to json
        name_spans = schedule_soup.find_all("#cal-parent:395910<>America/New_York appt-name")
        #iterate from json instead
        for name in name_spans:
            names.append(name.get_text())

        time_spans = schedule_soup.find_all("#cal-parent:395910<>America/New_York type-name")
        #iterate from json
        for time in time_spans:
            session_lengths.append(time.get_text())

        for name in names:
            spread[f"B{int(names.index(name))+int(27)}"] = item

        for name in names:
            spread[f"C{int(names.index(name))+int(27)}"] = name

        for session in session_lengths:
            spread[f"D{int(session_lengths.index(item))+int(27)}"] = session

        for time in session_lengths:
            if "45" in item:
                spread[f"E{int(session_lengths.index(item))+27}"] = .75
            elif "60" in item:
                spread[f"E{int(session_lengths.index(item))+27}"] = 1
            elif "75" in item:
                spread[f"E{int(session_lengths.index(item))+27}"] = 1.25
            else:
                spread[f"E{int(session_lengths.index(item))+27}"] = 1.5
    workdate_list.pop()
    names = []
    session_lengths = []
    cont = input("Enter another day?  Y/N  ")