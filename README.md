# TravelBlogApp
Travel blog app built using Flask and Python allows users to create and view travel notes for different countries. Users can input their travel notes and ratings, which are then stored in a CSV file. The app also queries the Restcountries API to display data for specific countries. 

# Features
- Displays a welcome message and navigation options.
- Allows users to select a country and see its details from the Restcountries API.
- Enables users to input a travel note for a specific country and give it a rating.
- Shows a list of all travel notes with country name, note, and rating details.
- Stores all travel notes and their details in a CSV file.
- Includes error handling for when the Restcountries API fails to retrieve data or when the CSV file is not found.
- Uses templates to render HTML pages with appropriate data and formatting.
- Uses the Restcountries API to fetch country details and display them to users.

# Prerequisites
- Python 3.x
- Flask

# Installation
1. Clone this repository to your local machine.
2. Navigate to the cloned directory.
3. Install the required dependencies.

# Usage
1. Start the Flask development server.
2. Open your web browser and go to http://localhost:5010.
3. The home page displays a list of all your travel notes. To add a new note, click on the "Add Note" button and fill in the form.
4. To edit an existing note, click on the "Edit" button next to the note you want to edit.
5. To delete an existing note, click on the "Delete" button next to the note you want to delete.
6. To view country details, click on the "Countries" button and enter the name of the country.

# CSV file
The travel notes are stored in a CSV file named "travel_notes.csv" in the root directory of the app.

# API
This app uses the Restcountries API to retrieve country data. If the API fails to retrieve data, an error message will be displayed.

# Contributing
Contributions are welcome! To contribute to the project, please follow these steps:

1. Fork the repository
2. Create a new branch
3. Make your changes and commit them
4. Push your changes to your forked repository
5. Create a pull request

# Author
Murat Ozder (muratozder@gmail.com)
