#Talking Data Starter Code

#Part 2 Setting up the program
import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
pd.set_option('max_colwidth', None)

movieData = pd.read_csv('./rotten_tomatoes_movies.csv')
favMovie = "Attack On Titan: Part 2 (Shingeki no kyojin endo obu za warudo)"
print("My Favorite movie is " + favMovie + ".")

# print(movieData.head())
# print(movieData["movie_title"])



#Part 3 Investigate the data



#Part 4 Filter data
print("\nThe data for my favorite movie is:\n")
#Create a new variable to store your favorite movie information

fav_movie_boolean_list = movieData["movie_title"] == favMovie
#print(fav_movie_boolean_list)

favMovieData = movieData.loc[fav_movie_boolean_list]
print(favMovieData)




print("\n\n")

#Create a new variable to store a new data set with a certain genre
horrormoviebooleanlist = movieData["genres"].str.contains("Horror")
horrormoviedata = movieData.loc[horrormoviebooleanlist]



numOfMovies = horrormoviedata.shape[0]

print("We will be comparing " + favMovie +
      " to other movies under the Horror genre in the data set.\n")
print("There are " + str(numOfMovies) + " movies under the category Horror.")

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
input("Press enter to see more information about how " + favMovie +
      " compares to other movies in Horror.\n")

#Part 5 Describe data
#min
min_rating = horrormoviedata["audience_rating"].min()
print("The min audience rating of the data set is: " + str(min_rating))
min_difference = 36 - min_rating
print(favMovie + " is " + str(min_difference) + " higher than the lowest rated movie.")
print()

#find max
max_rating = horrormoviedata["audience_rating"].max()
print("The max audience rating of the data set is: " + str(max_rating))
max_difference = max_rating - 36
print(favMovie + " is " + str(max_difference) +" points lower than the highest rated movie.")
print()

#find mean

mean = horrormoviedata["audience_rating"].mean()
print("The mean audience rating of the data set is: " + str(mean))
print(favMovie + " is lower than the mean movie rating.")

#find median

median = horrormoviedata["audience_rating"].median()
print("The median audience rating of the data set is: " + str(median))
print(favMovie + " is lower than the median movie rating.")

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
input("Press enter to see data visualizations.\n")

#Part 6 Create graphs
#Create histogram
plt.hist(horrormoviedata["audience_rating"], range = (0,100), bins = 20)

#Adds labels and adjusts histogram
plt.grid(True)
plt.title("Audience Ratings of Horror Movies Histogram")
plt.xlabel("Audience Ratings")
plt.ylabel("Number of Animation Movies")

#Prints interpretation of histogram
print(
  "According to the histogram, most movies fall under the rating from 20 to 40. The shape of the histogram is a bell curve which shows that it is most likely normally distributed. "
)
print()

#Show histogram
plt.show()
input("Press enter to see the next data visualization.\n")
plt.close()

#Create scatterplot
plt.scatter(data = horrormoviedata, x = "audience_rating", y = "critic_rating")
#Adds labels and adjusts scatterplot
plt.grid(True)
plt.title("Audience Rating vs Critic Rating")
plt.xlabel("Audience Rating")
plt.ylabel("Criitc Rating")
plt.xlim(0, 100)
plt.ylim(0, 100)

#Prints interpretation of scatterplot
print(
  "According to the scatter plot, there is a postive correlation with a direct pattern and some outliers exist. "
)
print()


#Show scatterplot
plt.show()

print("\nThank you for reading through my data analysis!")
