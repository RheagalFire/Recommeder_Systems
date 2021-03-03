
import pickle
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
import gzip

indices=pickle.load(open('indices.pickle','rb'))
cosine_sim=pickle.load(gzip.open('cosine_sim.pickle','rb'))
movies=pickle.load(open('movies.pickle','rb'))

def get_rec(title,cosine_sim=cosine_sim):
    #get the index
    idx=indices[title]
    # Get the pairwsie similarity scores of all movies with that movie
    similar_scores = list(enumerate(cosine_sim[idx]))
    #sort the movies based on sim_scores
    similar_scores=sorted(similar_scores,key=lambda x:x[1],reverse=True)
    #get the top 10 recommendations
    similar_scores=similar_scores[1:11]
    #get indices
    movie_indices=[i[0] for i in similar_scores]
    #return top 10 movies to the function 
    return indices.index[movie_indices]

def get_similar_movie(query):
    title_movie=movies['original_title']
    print(len(title_movie))
    title_movie[len(title_movie)]=query
    vectorizer = TfidfVectorizer()
    matrix_movies=vectorizer.fit_transform(title_movie)
    similar_movie=cosine_similarity(matrix_movies,matrix_movies)
    similar_scores_2= list(enumerate(similar_movie[len(title_movie)-1]))
    #sort the movies based on sim_scores
    similar_scores_2=sorted(similar_scores_2,key=lambda x:x[1],reverse=True)
    #get the top recommendation
    similar_scores_2_crop=similar_scores_2[1:2]
    #get indices
    movie_indices_2=[i[0] for i in similar_scores_2_crop]
    print(movie_indices_2)
    print(len(title_movie)-1)
    print(len(title_movie)-1 in movie_indices_2)
    if(len(title_movie)-1 in movie_indices_2):
        movie_indices_2=[i[0] for i in similar_scores_2[0:1]]
        return title_movie[movie_indices_2].values
    else:
        return title_movie[movie_indices_2].values

if __name__=="__main__":
    index=get_similar_movie('Harry Potter')
    print(get_rec(index[0]))
    print(get_rec("Batman"))







