from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty
import sqlite3
import japanize_kivy
import create_table

def create_participant(conn, participant):
    print(participant)
    sql = ''' INSERT INTO participant(year,no_of_events)
                  VALUES(?,?) '''
    cur = conn.cursor()
    cur.execute(sql, participant)
    conn.commit()
    return cur.lastrowid




class SurveyScreen(Screen):

    
    year = StringProperty("")
    events = StringProperty("")

    #入力したデータを記録する
    def insert_data(self, year, no_of_events):
        self.year = year.text
        self.events = no_of_events.text


class ResultScreen(Screen):
    age_text = StringProperty("")
    year_text = StringProperty("")
    events_text = StringProperty("")

    def submit_data(self, year, no_of_events):
        conn = sqlite3.connect("kivy_survey.db")
        participant_1 = (year, no_of_events)
        create_participant(conn, participant_1)

class ConfirmationScreen(Screen):
    pass

class TestApp(App):
    pass

if __name__ == '__main__':

    TestApp().run()

#dbファイルを作成
    sql_create_participant_table = ''' CREATE TABLE IF NOT EXISTS participant (
                                        id integer PRIMARY KEY,
                                        year text,
                                        no_of_events text
                                        ); '''
    conn = sqlite3.connect("kivy_survey.db")
    c = conn.cursor()
    create_table(conn, sql_create_participant_table)
