
import pickle
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
#import gzip

indices=pickle.load(open('indices.pickle','rb'))
#cosine_sim=pickle.load(gzip.open('cosine_sim.pickle','rb'))
movies=pickle.load(open('movies.pickle','rb'))

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
    print(str(index[0]))
    print(get_rec(index[0]))
    #print(get_rec("Batman"))
    print(get_rec('Avatar'))







