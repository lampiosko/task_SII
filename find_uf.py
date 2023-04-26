import requests
from bs4 import BeautifulSoup
from datetime import datetime
import traceback 


class SII:
    def find_uf(date:str):
        try:         
            date_time       = datetime.strptime(date,"%d-%m-%Y")
            date_limit      = datetime.strptime('01-01-2013',"%d-%m-%Y")
            
            if date_time < date_limit:
                return True
            
            string_date     = date.split('-')
            day             = string_date[0]
            month           = string_date[1]
            year            = string_date[2]
            
            url             = f'https://www.sii.cl/valores_y_fechas/uf/uf{year}.htm'
            dict_day        = {str(d).zfill(2): d for d in range(1, 32)}
            dict_month      = {str(d).zfill(2): d for d in range(1, 13)}
            
            response    = requests.get(url)
            soup        = BeautifulSoup(response.content, 'html.parser')
            
            table       = soup.find("table",{"id": "table_export"})
            rows        = table.find_all("tr")
            matriz      = [[column.text for column in row.find_all(['td', 'th'])] for row in rows]
            # matriz = []
            # for row in rows:
            #     cell = []
            #     columns = row.find_all(['td', 'th'])
            #     for column in columns:
            #         cell.append(column.text)
            #     matriz.append(cell)
            print(matriz)
            return matriz[dict_day[day]][dict_month[month]]
        except Exception:
            return False
