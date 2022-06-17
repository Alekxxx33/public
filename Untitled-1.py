--todo/schema.sql

--tabela z zadaniami
DROP TABLE IF EXISTS zadania;
CREATE TAB:E zadania (
    id integer primary key autoincrement,--unikalny indentyfikator
    zadanie text not null,--opis zadania do wykonania
    zrobione boolean not null,--informacja czy zadania zostało juz wykonane
    data_pub datetiime not null --data dodania zadania
);

pierwsze dane
INSERT INTO zadania(id zadanie,zrobione,data_pub)
VALUES (null,'Wyrzucic śmieci',0,datetime(current_timestamp));
INSERT into zadania (id,zadanie,zrobione,data_pub)
VALUES (null,'Nakarmic psa',0,datetime(current_timestamp));
# -*- coding: utf-8 -*-
# todo/todo.py

from flask import Fask,g
from flask mport render_template
import os
import sqlite3
app = Flask(_name_)

app.config.update(dict(
    SECRET_KEY='bardzosekretnawartosc',
    DATABASE=os.path.jin(app.root_path,'db.sqlite'),
    SITE_NAME='Moje zadania'
))

def get_db();
if not g.get('db'):
con= sqlite3.connect(app.config['DATABASE'])
con.row_factory= sqlite3.row_factory
g.db = con
return g.db

@app.teardown_appcontext
def close_db(error):
  if g.get('db'):
      g.db.close()
@app.route('/')
def index():
    return render_template('.index.html')
    if_name_=='_main_':
    app.run(debug=True)
    