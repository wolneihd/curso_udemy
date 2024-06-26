# valor: R$ 1.000.000
# pegou o empréstimo: 20/12/2020
# pagamento em 5 anos
# vencimento dia 20 de cada mês

from datetime import datetime
from dateutil.relativedelta import relativedelta

valor_emprestimo = 1_000_000
montante = 1_000_000
data_inicio = datetime.strptime('20/12/2020','%d/%m/%Y')
qtd_meses = 12*5
mes_atual = 0
ano_atual = data_inicio.year

while qtd_meses>0:    
    qtd_meses-=1
    mes_atual = data_inicio.month+1
    if mes_atual == 13:
        mes_atual = 1
        ano_atual = data_inicio.year + 1
    data_inicio = data_inicio + relativedelta(month=mes_atual, year=ano_atual)
    valor_mes = valor_emprestimo/60
    montante -= valor_mes
    print(data_inicio.strftime('%d/%m/%Y'), f'- Mensalidade: {valor_mes:.2f} - restante: {montante:.2f}' )

'''
from datetime import datetime
from dateutil.relativedelta import relativedelta

valor_total = 1_000_000
data_emprestimo = datetime(2020, 12, 20)
delta_anos = relativedelta(years=5)
data_final = data_emprestimo + delta_anos

data_parcelas = []
data_parcela = data_emprestimo
while data_parcela < data_final:
    data_parcelas.append(data_parcela)
    data_parcela += relativedelta(months=+1)

numero_parcelas = len(data_parcelas)
valor_parcela = valor_total / numero_parcelas

for data in data_parcelas:
    print(data.strftime('%d/%m/%Y'), f'R$ {valor_parcela:,.2f}')

print()
print(
    f'Você pegou R$ {valor_total:,.2f} para pagar '
    f'em {delta_anos.years} anos '
    f'({numero_parcelas} meses) em parcelas de '
    f'R$ {valor_parcela:,.2f}.'
)
'''