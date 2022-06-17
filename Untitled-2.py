@app.route('/zadania')
def zadania():
    db=get_db()
    kursor = db.execute('SELECT * FROM zadania ORDER BY data_pub DESC;')
    zadania = kursor.fetchall()
    return render_template('zadania_lista.html' zadania=zadania)
    @ app.route('/zrobione',metMods=['POST'])
    def zrobione():
        zadanie_id= request.form['id']
        db=get_db()
        db.execute('UPDATE zadania SET zrobione=1 WHERE id=?',[zadanie_id])
        db.commit()
        flash('Zmieniono status zadania.')
        return redirect(url_for('zadania'))
        