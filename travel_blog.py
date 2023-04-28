"""
Created on Sun Apr 16 21:32:01 2023

@author: muratozder
"""

from flask import Flask, render_template, request, redirect
import requests
import csv

app = Flask(__name__)

# set path for csv file
csv_file = 'travel_notes.csv'

# Read countries from the CSV file and create list of dictionaries with null note and rating > for add_note
country_list = []
with open(csv_file, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        if not row['note'] and not row['rating']:
            country = row['country']
            country_list.append(country)

# function to read travel notes from the csv file
def read_notes():
    travel_notes=[]
    try:
        with open(csv_file, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                travel_notes.append(row)
        return travel_notes
    except FileNotFoundError as e:
        with open(csv_file, 'w') as file:
            return travel_notes
    return travel_notes

# function to write travel notes to the csv file
def write_notes(travel_notes):
    with open(csv_file, 'w', newline='') as file:
        fieldnames = ['country', 'note', 'rating']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for note in travel_notes:
            writer.writerow(note)

# function showing count of countries visited
def count_countries_visited():
    with open('travel_notes.csv', 'r') as file:
        reader = csv.DictReader(file)
        countries_visited = set()
        for row in reader:
            if row['note']:
                countries_visited.add(row['country'])
        return len(countries_visited)


@app.route('/')
def home():
    travel_notes = read_notes()
    return render_template('index.html', travel_notes=travel_notes, count_countries_visited=count_countries_visited)

@app.route('/countries', methods=['GET', 'POST'])
def countries():
    if request.method == 'POST':
        country = request.form['country']
        # Query the restcountries API for country data
        response = requests.get('https://restcountries.com/v3.1/name/' + country)
        if response.status_code == 200:
            country_data = response.json()
            return render_template('country.html', country_data=country_data)
        else:
            return render_template('error.html', message='Failed to retrieve country data')
    return render_template('countries.html')

@app.route('/add_note', methods=['GET','POST'])
def add_note():
    if request.method == 'POST':
        country = request.form['country']
        note = request.form['note']
        rating = int(request.form['rating']) # Retrieve rating value
        new_travel_note = {'country': country, 'note': note, 'rating': rating}
        travel_notes = read_notes()
        travel_notes.append(new_travel_note)
        write_notes(travel_notes)
        return redirect('/')
    return render_template('add_note.html', country_list=country_list) 

@app.route('/edit_note/<int:index>', methods=['GET', 'POST'])  
def edit_note(index):
    travel_notes = read_notes()
    note = travel_notes[index]  
    if request.method == 'POST':
        country = request.form['country']  
        note = request.form['note']
        rating = int(request.form['rating'])
        travel_notes[index] = {'country': country, 'note': note, 'rating': rating}  
        write_notes(travel_notes)  
        return redirect('/')
    return render_template('edit_note.html', note=note, note_index=index)

@app.route('/delete_note/<int:index>')
def delete_note(index):
    travel_notes = read_notes()
    travel_notes.pop(index)
    write_notes(travel_notes)
    return redirect('/')

if __name__ == '__main__':
    #fixed the port 5010 to avoid clash while working
    app.run(debug=True, port=5010)