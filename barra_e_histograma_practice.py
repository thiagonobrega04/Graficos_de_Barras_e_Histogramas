# Curious about which book genres yield the highest sales at our cosmic bookstore? The given code produces a bar chart depicting sales data for different book genres. Click Run to view the sales visualization by genre!

import matplotlib.pyplot as plt
import numpy as np

genres = ['Fiction', 'Non-fiction', 'Children', 'Education', 'Mystery']  # Book genres
sales = [345, 290, 320, 415, 275]  # Sales per genre

plt.bar(genres, sales, color='purple')  # Create a bar plot with purple bars
plt.title('Sales by Genre in the Bookstore')
plt.xlabel('Genre')
plt.ylabel('Sales')
plt.show()

# It's time to make our bar plot even more interesting, Space Explorer! Did you know that we can rotate the bar plot? Try using the plt.barh function, where barh stands for "bar horizontal", instead of plt.bar function, and see what happens!

# Note that rotating graph means changing labels! So, make sure to swap x and y labels.

publishers = ['Alder', 'Birch', 'Cedar', 'Dogwood', 'Elm']
books_published = [23, 17, 35, 29, 14]

plt.barh(publishers, books_published, color='skyblue')  # Replace the bar with barh
plt.title('Number of Books Published per Publisher')
plt.ylabel('Publishers')
plt.xlabel('Books Published')
plt.show()

genres = ['Fiction', 'Non-Fiction', 'Children', 'Education', 'Mystery']
readers = [300, 250, 400, 150, 320]

# TODO: Create a bar plot to show the number of people who read each book genre.
plt.bar(genres, readers, color='purple')

# TODO: Set title 'Reading Habits: Number of People per Genre'
plt.title('Number of People per Genre')

# TODO: Set x label to 'Book Genres'
plt.xlabel('Book Genres')

# TODO: Set y label to 'Readers'
plt.ylabel('Readers')
plt.show()

# Imagine we have data on the ages of people who visit a bookstore. We want to determine at which age individuals engage most in reading. The provided code generates a histogram to present this information. Can you deduce how it does that? Click Run to view the distribution of the bookstore visitors' ages!

reading_ages = [15, 22, 35, 40, 8, 52, 23, 40, 30, 28, 36, 22]
bins = [0, 10, 20, 30, 40, 50, 60]

plt.hist(reading_ages, bins, edgecolor='black')
plt.title('Age Distribution of Book Readers')
plt.xlabel('Ages')
plt.ylabel('Number of Readers')
plt.show()

# Next challenge: let's visualize the reading habits at our bookstore. Fill in the blanks to show customers' reading durations. Remember, the histogram will reveal the pattern!

reading_time = np.random.normal(loc=5, scale=2, size=100)
# TODO: Create a list for the histogram bins representing hours intervals from 0 to 10
bins = [0, 2, 4, 6, 8, 10]
# TODO: Create histogram to show distribution of reading_time using plt.hist()
plt.hist(reading_time, bins, edgecolor='white')

plt.title('Reading Habits: Time Spent on Reading')
plt.xlabel('Hours')
plt.ylabel('Number of Customers')
plt.show()