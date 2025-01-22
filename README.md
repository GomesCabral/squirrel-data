# Squirrel Color Count

This Python script processes squirrel data from a CSV file to count the number of squirrels based on their primary fur color. The result is stored in a new CSV file with the counts of each color (Gray, Red, and Black).

## Features
- **Data Processing**: Reads a CSV file containing squirrel data.
- **Color Counting**: Counts the number of squirrels for each primary fur color (Gray, Cinnamon, and Black).
- **CSV Output**: Outputs the results into a new CSV file containing the color count for each category.

## Technologies Used
- **Python**: The programming language used for this script.
- **Pandas**: A Python library used for reading and manipulating CSV data.

## Requirements
Before running the script, make sure you have the following libraries installed:

```bash
pip install pandas
````
Usage
Clone this repository to your local machine:
  git clone https://github.com/your-username/squirrel-color-count.git
Make sure you have the necessary input CSV file (squirrel_data.csv) in the same directory as the script. This file should have a column named Primary Fur Color containing the fur color of each squirrel.

Run the script:
  python squirrel_color_count.py

How the Script Works
Reading the CSV: The script loads the squirrel data from the squirrel_data.csv file using the pandas.read_csv method.
Color Counting: It extracts the "Primary Fur Color" column and counts the number of occurrences of each fur color (Gray, Cinnamon, and Black).
Data Storage: The counts are stored in a dictionary and converted into a Pandas DataFrame.
Output CSV: The results are saved into a new CSV file (squirrel_count_by_color.csv) which lists each color and its corresponding count.
Example of squirrel_count_by_color.csv
The generated CSV file will look like this:

Color, Count
grey, 120
red, 45
black, 30
