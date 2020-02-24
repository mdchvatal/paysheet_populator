import ezsheets
import requests

workdate_list = []
cell_counter = 27

login_data = {
    "username": "",
    "password": "",
}

date = input("Enter URL of pay spreadsheet:  ")
ss = ezsheets.Spreadsheet(date)
spread = ss[0]
#change? url encode?

cont = input("Enter a work date? Y/N  ")
while cont == "Y":
    schedule_date = str(input("Which date? (yyyy-mm-dd)  "))
    workdate_list.append(schedule_date)
    cont = input("Add another day? (Y/N)  ")

for date in workdate_list:
    payload = {"minDate": date, "maxDate": date, "calendarID": "395910"}
    req = requests.get("https://acuityscheduling.com/api/v1/appointments", params=payload, auth=(login_data["username"], login_data["password"]))
    schedule_soup = req.json()
    for item in schedule_soup:
        spread[f"B{int(cell_counter)}"] = date
        spread[f"C{int(cell_counter)}"] = str(schedule_soup[schedule_soup.index(item)]["firstName"]+" "+schedule_soup[schedule_soup.index(item)]["lastName"])
        spread[f"D{int(cell_counter)}"] = schedule_soup[schedule_soup.index(item)]["type"]
        if "45" in schedule_soup[schedule_soup.index(item)]["type"]:
            spread[f"E{int(cell_counter)}"] = .75
        elif "60" in schedule_soup[schedule_soup.index(item)]["type"]:
            spread[f"E{int(cell_counter)}"] = 1
        elif "75" in schedule_soup[schedule_soup.index(item)]["type"]:
            spread[f"E{int(cell_counter)}"] = 1.25
        else:
            spread[f"E{int(cell_counter)}"] = 1.5
        cell_counter += 1
        
