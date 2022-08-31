import datareader as datareader
from openpyxl import Workbook, load_workbook
import datetime as dt
import pandas_datareader as convert


def main():
    workbook = load_workbook('Player Profiles.xlsx')
    worksheet = workbook.active
    worksheet.title = "Players"

    add_players(worksheet)

    workbook.save('Player Profiles.xlsx')


def add_players(worksheet):
    worksheet['A2'] = "Vinicius Junior"
    worksheet['B2'] = "12/07/2000"
    worksheet['D2'] = 5000000
    worksheet['E2'] = 3000000
    worksheet['J2'] = 151
    worksheet['K2'] = 40
    worksheet['L2'] = 21
    worksheet['M2'] = 302
    worksheet['N2'] = 180

    worksheet['A3'] = "Karim Benzema"
    worksheet['B3'] = "19/12/1987"
    worksheet['D3'] = 10000000
    worksheet['E3'] = 10000000
    worksheet['J3'] = 450
    worksheet['K3'] = 342
    worksheet['L3'] = 193
    worksheet['M3'] = 902
    worksheet['N3'] = 692

    worksheet['A4'] = "Luka Modric"
    worksheet['B4'] = "09/09/1985"
    worksheet['D4'] = 12000000
    worksheet['E4'] = 8000000
    worksheet['J4'] = 653
    worksheet['K4'] = 54
    worksheet['L4'] = 89
    worksheet['M4'] = 293
    worksheet['N4'] = 150

    for row in range(2, len(worksheet['B']) + 1):
        today = dt.datetime.now()

        print(len(worksheet['B']))

        print(worksheet[f'B{row}'].value)
        birthdate = dt.datetime.strptime(worksheet[f'B{row}'].value, "%d/%m/%Y")
        age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))

        worksheet[f'C{row}'] = age
        worksheet[f'F{row}'] = worksheet[f'D{row}'].value + worksheet[f'E{row}'].value

        usd_to_eur = convert.get_data_fred('DEXUSEU').iloc[-1]['DEXUSEU']
        worksheet[f'G{row}'] = worksheet[f'F{row}'].value / usd_to_eur

        conversion_rate = float(worksheet[f'K{row}'].value) / float(worksheet[f'M{row}'].value)
        worksheet[f'O{row}'] = round(conversion_rate, 2)

        goals_per_game = float(worksheet[f'K{row}'].value) / float(worksheet[f'J{row}'].value)
        worksheet[f'P{row}'] = round(goals_per_game, 2)

        assists_per_game = float(worksheet[f'L{row}'].value) / float(worksheet[f'J{row}'].value)
        worksheet[f'Q{row}'] = round(assists_per_game, 2)

        contributions = (float(worksheet[f'L{row}'].value) + float(worksheet[f'K{row}'].value)) / float(worksheet[f'J{row}'].value)
        worksheet[f'R{row}'] = round(contributions, 2)

        goals_per_assist = float(worksheet[f'K{row}'].value) / float(worksheet[f'L{row}'].value)
        worksheet[f'S{row}'] = round(goals_per_assist, 2)








if __name__ == '__main__':
    main()
