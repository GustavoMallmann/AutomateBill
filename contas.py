import openpyxl
import numpy as np
import pandas as pd

if __name__ == '__main__':
    aluguel = 1000.0
    energia = 100.0
    internet = 50.0
    caixa = 100
    #notas = input('Digite o valor das notas:(G J R)').split()
    notas = (10.0, 20.0, 30.0)

    s_nomes = np.array(['Gustavo', 'Japa', 'Roberto'])
    s_aluguel = np.full(3, aluguel/3)
    s_energia = np.full(3, energia/3)
    s_internet = np.full(3, internet/3)
    s_caixa = np.full(3, caixa/3)
    s_total_sm = s_aluguel + s_energia + s_internet + s_caixa
    s_notas = np.array(notas, dtype=float)
    dist_notas = np.sum(s_notas)
    s_dist_notas = np.full(3, dist_notas/3)
    s_total_cm = s_total_sm + s_dist_notas - s_notas

    data = {'Nome': s_nomes,
            'Aluguel': s_aluguel,
            'Energia': s_energia,
            'Internet': s_internet,
            'Caixa': s_caixa,
            'Total sem mercado': s_total_sm,
            'Notas': s_notas,
            'Distribuição de notas': s_dist_notas,
            'Total': s_total_cm
            }
    df = pd.DataFrame(data=data).round(2)
    print(df)
    writer = pd.ExcelWriter('tabelateste.xlsx', engine='xlsxwriter')
    df.to_excel(writer, sheet_name='contas', index=False)  # send df to writer
    worksheet = writer.sheets['contas']  # pull worksheet object
    for idx, col in enumerate(df):  # loop through all columns
        series = df[col]
        max_len = max((
            series.astype(str).map(len).max(),  # len of largest item
            len(str(series.name))  # len of column name/header
        )) + 1  # adding a little extra space
        worksheet.set_column(idx, idx, max_len)  # set column width
    obs = input('Alguma observação?')
    if obs != "":
        worksheet.write(5, 0, 'OBS:')
        worksheet.write(5, 1, obs)
    writer.save()
    #df.to_excel('tabelateste.xlsx', index=False)
# trocar np.array por pd.series
