from bs4 import BeautifulSoup
import requests
import database


req = requests.get("https://www.vssut.ac.in/notice-board.php?page=1")
# req.status_code
print(req.status_code)

soup = BeautifulSoup(req.text, 'html.parser')

table_contents = soup.table
table_body = table_contents.tbody

table_rows=table_body.find_all('tr')
# print(table_rows)

for table_row in table_rows:
    cols_sl_no = table_row.find('td', attrs={"data-title": "S.N."})
    cols_title = table_row.find('td', attrs={"data-title": "Title"})
    cols_date = table_row.find('td', attrs={"data-title": "Date"})
    cols_link = "https://vssut.ac.in/"
    cols_link += table_row.find('td', attrs={"data-title": "View"}).a['href']

    # to save data in to the database
    database.SaveData(cols_date.text, cols_title.text, cols_link)




    # cols_sl_no=table_col
    # cols_title=table_cols[1].text
    # cols_date=table_cols[2].text
    # cols_link="https://vssut.ac.in/"+table_cols[3].a['href']
    print(cols_link, cols_date)


