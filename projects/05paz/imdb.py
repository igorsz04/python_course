import pandas as pd


df = pd.read_csv('~/Downloads/movie_metadata.csv', index_col='movie_title')
#print(df.info())
#print('df shape \n', df.shape)
print('df is null sum\n', df.isnull().sum())

print(df.shape)
temp_df = df.append(df.tail(1000))
temp_df = temp_df.drop_duplicates()
print(temp_df.shape)


print(df.columns)

print('budget')
budget = df['budget'].dropna()
print('budget mean\n')
print(budget.mean())

print(df['genres'].value_counts().head(20))

print('Ridley Scott')
ridley_movies = df[df['director_name'] == 'Ridley Scott']
print(ridley_movies.head())

print('df kolumny',df.columns)
print(df['actor_1_facebook_likes'].max())
likes_mean = df['actor_1_facebook_likes'].mean()
most_facebook_likes_actors = df[df['actor_1_facebook_likes'] > likes_mean]
print(most_facebook_likes_actors['actor_1_facebook_likes'].count())
print('\n most liked actors long movies \n')
most_liked_actors_long_movies = df[
    (df['actor_1_facebook_likes'] > likes_mean) &
    (df['duration'] > 60)
]

print(most_liked_actors_long_movies['actor_1_facebook_likes'].count())

print('movies between 2005-2010 with imdb score more than its median (without nans, 0s)')
movies_between = df[
    (df['title_year'] > 2004) &
    (df['title_year'] < 2011) &
    (df['imdb_score'] > df['imdb_score'].median())
]

columns = ['title_year','imdb_score']
print(movies_between[columns])
print(movies_between['title_year'].count())

print(movies_between.groupby('title_year').count()['imdb_score'])

print('funkcja rating function')
def rating_function(x):
    if x>=8.0:
        return "good"
    else:
        return "bad"


#count good and bad movies
rated_movies = movies_between['imdb_score'].apply(rating_function)
print(rated_movies.value_counts())


print('get title of max rated movie')
max_rated_movie_index = movies_between['imdb_score'].values.argmax()
print(max_rated_movie_index)
print(movies_between.ix[max_rated_movie_index])

import matplotlib.pyplot as plt
df1 = df[df['budget'] > 2000000]
#movies_between.plot(kind='scatter', x='imdb_score', y='budget', title='rating vs budget')
#df1['imdb_score'].plot(kind='hist', title='Score')
#df1['imdb_score'].plot(kind='box')

# plot histograms for movies from 2008, 2009, 2010, 2011 in subplots
def plot_histograms():
    plot_2008 = df[df['title_year'] ==2008]['imdb_score']
    plot_2009 = df[df['title_year'] ==2009]['imdb_score']
    plot_2010 = df[df['title_year'] ==2010]['imdb_score']
    plot_2011 = df[df['title_year'] ==2011]['imdb_score']

    fig, axes = plt.subplots(nrows=2, ncols=2)
    plot_2008.plot(ax=axes[0,0], kind='hist')
    plot_2009.plot(ax=axes[0,1], kind='hist')
    plot_2010.plot(ax=axes[1,0], kind='hist')
    plot_2011.plot(ax=axes[1,1], kind='hist')
    plt.show()

#plot_histograms()

#plot genres count as bar plot
genres = df['genres'].value_counts()
genres[df['title_year']].plot(kind='bar')
plt.show()