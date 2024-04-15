# Introduction and Overview
# Welcome to this interactive lesson on bar plots and histograms in Python! In this lesson, we will embark on a beautiful data visualization journey. We will focus on constructing bar plots and histograms using Matplotlib.

# Building Bar Plots with Matplotlib
# A bar plot visually represents categorical data as rectangular bars, the lengths of which are proportional to their respective values. For instance, a bar plot would be the ideal choice if we wanted to visualize a bookstore's sales data, where the categories are book names and the values are sales numbers.

# We can build a bar plot using plt.bar function, which takes in two arrays of the same length: category names and values per category.

import matplotlib.pyplot as plt

books = ['Book1', 'Book2', 'Book3', 'Book4', 'Book5']   # Book names
sales = [123, 432, 567, 245, 312]            # Corresponding number of copies sold

plt.bar(books, sales)                        # Create bar plot
plt.title('Book Sales')
plt.xlabel('Books')
plt.ylabel('Number of Sold Copies')
plt.show()

# Building Histograms with Matplotlib: Dataset
# Now, let's move on to histograms! Unlike bar plots, histograms are designed for visualizing distributions of continuous, numeric data. In a histogram, bars represent the frequency of data points falling under specific ranges or bins. Let's say we have age data for a city's population for this example.

# Generates a data set with 150 data points, with a mean of 27 and standard deviation of 12
import numpy as np

ages = np.random.normal(loc=27, scale=12, size=150) 

#Creates 6 bins that are left inclusive, right exclusive
#Bin 1: [0,10), Bin 2: [10,20), and so on
bins = [0, 10, 20, 30, 40, 50, 60]

# Building Histograms with Matplotlib: Plot
# We'll use this data to create a histogram that visualizes the age distribution.

plt.hist(ages, bins, edgecolor='black')   # Create histogram
plt.title('Ages in City X')
plt.xlabel('Ages')
plt.ylabel('Number of People')
plt.show()

# Distinguishing Between Bar Plots and Histograms
# While they may possess visual similarities, bar plots and histograms offer distinct data views. Bar plots excel when displaying categorical data, whereas histograms provide insights into numerical data distributions.