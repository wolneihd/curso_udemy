from datetime import datetime
#ano,mes,dia,hora,min,seg.
data = datetime(2022,4,20,7,49,25)
print(data)
#--------------
data_str_data = '2022-04-20 07:49:23'
data_str_format = '%Y-%m-%d %H:%M:%S'
data = datetime.strptime(data_str_data,data_str_format)
print(data)
