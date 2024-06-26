# pip install pytz
# pip install types-pytz

from datetime import datetime
from pytz import timezone 

data = datetime.now(timezone('America/Sao_Paulo'))
print(data)

data = datetime.now(timezone('Asia/Tokyo'))
print( data)

data = datetime(2022,4,20,7,49,25, tzinfo=timezone('Asia/Tokyo'))
print(data)

data = datetime.now()
print(data.timestamp()) # número segundos desde 01.01.1970
print(data.fromtimestamp(1670849124))
