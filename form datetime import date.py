form datetime import date
from flask import flash,redirect,url_for ,request

@app.route('/zadania',methods=['GET','POST""'])
def zadania();
error= None
if request.method == 'POST':
    zadanie = request.form['zadanie'].strip()
    if len(zadanie) > 0:
        zrobione = '0'
        data_pub= datetime.now()
        db= get_db()
        db.execute('INSERT INTO zadania VALUES? ? ?? ,'_
        [None,zadanie,zrobione,data_pub])
        db.commit()
        flash('Dodano nowe zadanie.')
        return redirect(url_for('zadania'))
        error = 'Nie mozesz doadac pustego zadania'

db= get-db()
kursor= db.execute('SELECT *FROM zadania ORDER BY data_pub DESC')
zadania = kursor.fetchall*(
    return render_template('zadania_lista.html' zadania= zadania, error= error)
    
)