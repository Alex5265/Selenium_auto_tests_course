from datetime import datetime
patern = '%H:%M'
n = "10:00-11:00"

st, en = n.split('-')
st = datetime.strptime(st, patern)
en = datetime.strptime(en, patern)
print(st.hour)