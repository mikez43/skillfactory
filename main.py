per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

money = int(input())

deposit = list(per_cent.values())

def profit(x):
    perc = round(x / 100 * money)
    return perc

deposit = list(map(profit, deposit))

print(deposit)
print('Максимальная сумма, которую вы можете заработать — ' + str(max(deposit)))