# Geographic-Analysis
Plot the locations of restaurants on a map using longitude and latitude coordinates. Identify any patterns or clusters of restaurants in specific areas.

Restaurant Data Analysis
This project is a Tkinter-based application for analyzing restaurant data from a CSV file. It includes geographic analysis to plot the locations of restaurants on a map and identify patterns or clusters.

Features
Geographic Map of Restaurants: Plots restaurant locations on a map using folium.
Restaurant Clusters Analysis: Visualizes the geographic distribution of restaurants and identifies clusters using scatter plots.
Graphical Visualizations: Provides an interactive map and scatter plots to explore the data.
Prerequisites
Python 3.x
pandas
tkinter
folium
matplotlib
seaborn
Installation
Clone the repository:
bash

cd restaurant-data-analysis
Install the required libraries:
bash
Copy code
pip install pandas tkinter folium matplotlib seaborn
Usage
Make sure your dataset CSV file is properly formatted and placed in the correct directory. Update the file path in the script if necessary.
Run the script:
bash
Copy code
python main.py
Code Overview
Data Loading
The dataset is loaded using pandas.read_csv and processed to extract geographic information.

Tkinter Interface
A Tkinter window is created to display the results. The interface includes buttons to open separate windows for each type of analysis.

Folium and Seaborn Visualizations
Folium: Used to create interactive maps with markers for each restaurant.
Seaborn: Used to create scatter plots for analyzing geographic clusters of restaurants.
Dataset
Ensure that your dataset CSV file contains at least the following columns:

Restaurant Name: The name of the restaurant.
Latitude: The latitude coordinate of the restaurant.
Longitude: The longitude coordinate of the restaurant.
City: The city where the restaurant is located.
Example Dataset
Here's a snippet of what your dataset might look like:

csv
Copy code
Restaurant Name,Latitude,Longitude,City
Restaurant A,12.9715987,77.594566,City1
Restaurant B,28.704060,77.102493,City2
Restaurant A,12.9715987,77.594566,City1
...
License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgements
This project was developed by [Nitin jain].
Special thanks to the open-source community for providing the necessary libraries and tools.
