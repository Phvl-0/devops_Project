from datetime import datetime

depart1 = "I left home at: "
depart2 = "I will be there by: "
depart3 = "You should get here by: "

def qwe(depart):
    print(f"{depart}{datetime.now().strftime('%H:%M:%S')}")

qwe(depart1)
qwe(depart2)
qwe(depart3)