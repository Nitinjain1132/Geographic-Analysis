import pandas as pd
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import seaborn as sns
import folium
from folium.plugins import MarkerCluster

# Load the dataset
data = pd.read_csv(r"C:\Users\HP\Desktop\kartik\Dataset .csv")

# Function to create a window with the folium map
def map_window():
    window = tk.Toplevel(root)
    window.title("Geographic Analysis")
    window.geometry("800x600")

    # Create a base map
    map_center = [data['Latitude'].mean(), data['Longitude'].mean()]
    restaurant_map = folium.Map(location=map_center, zoom_start=12)

    # Add markers to the map
    marker_cluster = MarkerCluster().add_to(restaurant_map)
    for _, row in data.iterrows():
        folium.Marker(location=[row['Latitude'], row['Longitude']],
                      popup=row['Restaurant Name']).add_to(marker_cluster)

    # Save the map to an HTML file
    map_file = 'restaurant_map.html'
    restaurant_map.save(map_file)

    # Load the map into a tkinter window
    map_label = tk.Label(window)
    map_label.pack(fill=tk.BOTH, expand=True)
    map_label.html = tk.HTMLLabel(window, html=open(map_file).read())
    map_label.html.pack(fill=tk.BOTH, expand=True)

# Function to analyze and plot restaurant clusters
def cluster_analysis_window():
    window = tk.Toplevel(root)
    window.title("Restaurant Clusters Analysis")
    window.geometry("800x600")

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.scatterplot(data=data, x='Longitude', y='Latitude', hue='City', ax=ax, palette="viridis", s=50)
    ax.set_title('Geographic Distribution of Restaurants')
    ax.set_xlabel('Longitude')
    ax.set_ylabel('Latitude')

    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

# Create the main window
root = tk.Tk()
root.title("Restaurant Data Analysis")
root.geometry("400x300")

# Apply a theme
style = ttk.Style(root)
style.theme_use('clam')

# Set up font and colors
root.option_add("*Font", "Helvetica 12")
style.configure("TButton", padding=6, relief="flat", background="#ccc")
style.map("TButton", background=[('active', '#0052cc')], foreground=[('active', 'white')])

# Create a frame
frame = ttk.Frame(root, padding="20")
frame.pack(fill=tk.BOTH, expand=True)

# Title label
title_label = ttk.Label(frame, text="Restaurant Data Analysis", font=("Helvetica", 16, "bold"))
title_label.pack(pady=10)

# Create buttons to open each graph window
ttk.Button(frame, text="Geographic Map of Restaurants", command=map_window).pack(padx=10, pady=10)
ttk.Button(frame, text="Restaurant Clusters Analysis", command=cluster_analysis_window).pack(padx=10, pady=10)

# Start the main event loop
root.mainloop()
