# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 14:59:47 2024

@author: Omphulusa Nelwamondo
"""

import pandas as pd

df = pd.read_csv("movie_dataset (1).csv")
#print(df)
RatingMax_Idx = df["Rating"].idxmax()
Most_watched_movie = df["Title"][RatingMax_Idx]
print(Most_watched_movie)
# Answer Q1 = The dark Knight
#================================================

average_revenue = df['Revenue (Millions)'].mean()
print(average_revenue)
print(average_revenue)
#Answer Q2 = 82.95637614678898(million)

filtered_df = df[(df['Year'] >= 2015) & (df['Year'] <= 2017)]
average_revenue_2015_2017 = filtered_df['Revenue (Millions)'].mean()
print(average_revenue_2015_2017)
#Answer Q3 = 63.099905660377345 (million)

# Filter the dataframe for movies released in 2016
movies_2016 = df[df['Year'] == 2016]
num_movies_2016 = len(movies_2016)
print(num_movies_2016)
#Answer Q4 = 297

number_of_movies_directed_by_Christopher = df[df['Director'] == 'Christopher Nolan'].shape[0]
print(number_of_movies_directed_by_Christopher)
#Answer Q5 = 5

number_of_high_rated_movies = df[df['Rating'] >= 8.0].shape[0]
print(number_of_high_rated_movies)
#Answer Q6 = 78

Christopher_movies = df[df['Director'] == 'Christopher Nolan']
median_rating_Christopher_directed = Christopher_movies['Rating'].median()
print(median_rating_Christopher_directed)
#Answer Q7 = 8.6

yearly_average_rating = df.groupby('Year')['Rating'].mean()
year_with_highest_rating = yearly_average_rating.idxmax()
print(year_with_highest_rating)
#Answer Q8 = 2007


number_of_movies_in_2006 = df[df['Year'] == 2006].shape[0]
number_of_movies_in_2016 = df[df['Year'] == 2016].shape[0]
percentage_increase = ((number_of_movies_in_2016 - number_of_movies_in_2006) / number_of_movies_in_2006) * 10
print(percentage_increase)
#Answer Q9 =575 (%)

from collections import Counter
all_actors = df['Actors'].str.split(', ').sum()
actor_counts = Counter(all_actors)
most_common_actor = actor_counts.most_common(1)[0]
print(most_common_actor)
#Answer Q10 = Mark Wahlberg

unique_genres = set(df['Genre'].str.split(',').explode())
number_of_unique_genres = len(unique_genres)
print(number_of_unique_genres)
#Answer Q11 = 20

















