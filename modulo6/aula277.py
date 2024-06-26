from datetime import datetime

fmt = '%d/%m/%Y'
data = datetime.strptime('2022-12-13 07:59:23','%Y-%m-%d %H:%M:%S')

# Vai alterar para o formato desejado!
print(data.strftime(fmt))

print(data.strftime('%d/%m/%Y %H:%M'))
print(data.strftime('%d/%m/%Y %H:%M:%S'))

print(data.strftime('%Y'),data.year)
print(type(data.strftime('%Y')),type(data.year))

print(data.strftime('%d'),data.day)
print(data.strftime('%m'),data.month)