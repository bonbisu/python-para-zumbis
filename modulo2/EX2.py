# Considere a empresa de telefonia Tchau.
# Abaixo de 200 minutos, a empresa cbra R$ 0,20 por minuto.
# Entre 200 e 400 minutos, o preço é R$ 0,18.
# Acima de 400 minutos o preço por minuto é R$ 0,15. Calcule sua conta de telefone.

minutos_gastos = int(
    input('Insira a quantidade de minutos utilizads esse mes: '))
if minutos_gastos <= 200:
    print('Total a pagar R$ %5.2f' % (minutos_gastos*0.2))
else:
    if minutos_gastos > 200 and minutos_gastos <= 400:
        print('Total a pagar R$ %5.2f' % (minutos_gastos*0.18))
    else:
        if minutos_gastos > 400:
            print('Total a pagar R$ %5.2f' % (minutos_gastos*0.15))
