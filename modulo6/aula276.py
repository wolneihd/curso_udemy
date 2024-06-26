from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

fmt = '%d/%m/%Y %H:%M:%S'

data_inicio = datetime.strptime('20/04/1987 09:30:30', fmt)
data_fim = datetime.strptime('12/02/2022 08:20:00', fmt)

print(data_inicio > data_fim)
print(data_inicio < data_fim)
delta = data_fim - data_inicio
print(delta.days, delta.seconds)
delta = timedelta(days=10, hours=2)
print(data_fim + delta)

# pip install python-dateutil types-python-dateutil
# from dateutil.relativedelta import relativedelta
# permite mais opções de variáveis para editar data
# para mais - documentação de 'dateutil' e 'timedelta'

print(data_fim + relativedelta(seconds=87))
print(relativedelta(data_fim, data_inicio))