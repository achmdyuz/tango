#!/usr/bin/env python3
#-*- coding: utf-8 -*- # Setup characters encode to "UTF-8"
from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

DATABASE = 'db/tango.db'

def get_db_connection():
    return sqlite3.connect(DATABASE)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create', methods=['POST'])
def create_entry():
    if request.method == 'POST':
        tango = request.form['tango']
        yomiKata = request.form['yomiKata']
        imi = request.form['imi']
        nichiji = request.form['nichiji']

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO tango (tango, yomiKata, imi, nichiji) VALUES (?, ?, ?, ?)",
                       (tango, yomiKata, imi, nichiji))
        conn.commit()
        conn.close()

        return redirect(url_for('index'))

@app.route('/read')
def read_entries():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tango")
    entries = cursor.fetchall()
    conn.close()

    return render_template('read.html', entries=entries)

# Add routes for update and delete functions

@app.route('/update/<int:tango_id>', methods=['GET', 'POST'])
def update_entry(tango_id):
    if request.method == 'POST':
        tango = request.form['tango']
        yomiKata = request.form['yomiKata']
        imi = request.form['imi']
        nichiji = request.form['nichiji']

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE tango SET tango = ?, yomiKata = ?, imi = ?, nichiji = ? WHERE tango_id = ?",
                       (tango, yomiKata, imi, nichiji, tango_id))
        conn.commit()
        conn.close()

        return redirect(url_for('read_entries'))

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tango WHERE tango_id = ?", (tango_id,))
    entry = cursor.fetchone()
    conn.close()

    return render_template('update.html', entry=entry)
    
@app.route('/search', methods=['GET', 'POST'])
def search_entries():
    if request.method == 'POST':
        search_query = request.form['search_query']
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tango WHERE tango LIKE ? OR yomiKata LIKE ? OR imi LIKE ?",
                       (f"%{search_query}%", f"%{search_query}%", f"%{search_query}%"))
        results = cursor.fetchall()
        conn.close()
        return render_template('search_results.html', results=results, search_query=search_query)
    
    return render_template('search.html')
    
@app.route('/delete/<int:tango_id>')
def delete_entry(tango_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tango WHERE tango_id = ?", (tango_id,))
    conn.commit()
    conn.close()

    return redirect(url_for('read_entries'))
if __name__ == '__main__':
    app.run(debug=True)

