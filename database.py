import os

from dotenv import load_dotenv
import mysql.connector
import telegram

load_dotenv()

mydb = mysql.connector.connect(
    host=os.getenv('DB_HOST'),
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSWORD'),
    database=os.getenv('DB_DATABASE')
)


# Define a class to call it in another position remember class Name starte with CAPITAL
class SaveData:
    def __init__(self, date, title, link):
        self.date = date
        self.title = title
        self.link = link

        # Define the variables to operate the function
        # my_link="https://mabia.in/112"
        # my_date="2022-06-13"
        # my_title="Test Title112"

        mycursor = mydb.cursor()

        # Create query for checking if the unique link is already present in the database
        sql_chk = "SELECT * FROM vssut_1 WHERE link='" + self.link + "'"

        # try to execute the query else get the exception
        try:
            mycursor.execute(sql_chk)
            mycursor.fetchall()
            print(mycursor.rowcount, "record exits")
        except mysql.connector.IntegrityError as err:
            print("Error: {}".format(err))

        if mycursor.rowcount < 1:
            sql = "INSERT INTO vssut_1 ( date, title, link) VALUES (%s, %s, %s)"
            val = (self.date, self.title, self.link)
            try:
                mycursor.execute(sql, val)
                mydb.commit()
                # to send telegram message to a CHAT_ID
                telegram.SendTelegram(self.date, self.title, self.link)
                print(mycursor.rowcount, "record inserted.")
            except mysql.connector.IntegrityError as err:
                print("Error: {}".format(err))

# p1=SaveData("2022-06-13","Title222","https://mabia.in/222")
