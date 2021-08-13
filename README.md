# paysheet_populator
This is a python app for populating a Google Sheet with information from the scheduling website Acuity's back-end API. Much quicker and less tedious than doing it by hand!

Note: The "username" and "password" values within the dictionary "login_data" are left blank in this copy. They are hard-coded with
API key data from Acuity's API side, as I am the only person using this particular application. Also, the EZSheets library automatically pulls authentication data from the directory in which the
app is housed. To use this app, you have to download google Drive's and Sheets' pickles into the directory as well as your Google credentials' JSON. EZsheets accesses them automatically. 
