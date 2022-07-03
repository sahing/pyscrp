from bs4 import BeautifulSoup
import requests

# import database

# req = requests.get("https://www.vssut.ac.in/notice-board.php")
# # req.status_code
# print(req.status_code)
#
# soup = BeautifulSoup(req.text, 'html.parser')
#
# table_contents= soup.table
# table_body=table_contents.tbody
#
# table_rows=table_body.find_all('tr')
# # print(table_rows)
#
# for table_row in table_rows:
#     cols_sl_no = table_row.find('td', attrs={"data-title": "S.N."})
#     cols_title = table_row.find('td', attrs={"data-title": "Title"})
#     cols_date = table_row.find('td', attrs={"data-title": "Date"})
#     cols_link = "https://vssut.ac.in/"
#     cols_link+=table_row.find('td', attrs={"data-title": "View"}).a['href']
#
#     # to save data in to the database
#     p1 = database.SaveData(cols_date.text, cols_title.text, cols_link)
#
#
#     # cols_sl_no=table_col
#     # cols_title=table_cols[1].tet
#     # cols_date=table_cols[2].text
#     # cols_link="https://vssut.ac.in/"+table_cols[3].a['href']
#     print(cols_link,cols_date)


def get_result(roll_no1)
roll_no1=str(070000000)
url = "http://wbresults.org.in/view_resultt.php?roll_no="+roll_no1+"&submit=submit"

payload={}
headers = {
  'Cookie': 'PHPSESSID=31a4d5d346f6e0bad1250870c479df6d'
}

response = requests.request("POST", url, headers=headers, data=payload)

soup = BeautifulSoup(response.text,'html.parser')
tables=soup.find_all('table')


# print(response.text)
# print(soup.table)
# print(tables[3])
print(soup)

