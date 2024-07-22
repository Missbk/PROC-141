from flask import Flask, jsonify
import pandas as pd

movies_data = pd.read_csv('final.csv')

app = Flask(__name__)

# extraer información importante de dataframe


# variables para almacenar información



# método para obtener información de la base de datos
def assign_val():
  m_data ={
    
    "duration":all_movies.iloc[0,3],
    "rating":all_movies.iloc[0,4]/2
   }
  return m_data


 
# /movies api
@app.route("/movies")



# /like api
@app.route("/like")




   



# /dislike api
@app.route("/dislike")
#Quitar a partir de aqui
def unliked_movie():
   global all_movies

   movie_data= assign_val()
   not_liked_movies.append(movie_data)
   all_movies.drop([0], inplace =True)
   all_movies=all_movies.reset_index(drop=True)
   
   return jsonify({
      "status": "success"
   })

# /did_not_watch api
@app.route("/did_not_watch")#se cambió por /not_seen

def did_not_watch_view():
   global all_movies

   movie_data= assign_val()
   did_not_watch.append(movie_data)
   all_movies.drop([0], inplace =True)
   all_movies=all_movies.reset_index(drop=True)
   return jsonify({
      "status": "success"
   })

if __name__ == "__main__":
  app.run()
