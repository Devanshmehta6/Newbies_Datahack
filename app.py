from flask import Flask,render_template, request
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import pickle, pandas
popular_df = pickle.load(open('new.pkl','rb'))
pt = pickle.load(open('pt.pkl','rb'))
# books = pickle.load(open('books.pkl','rb'))
similarity_scores = cosine_similarity(pt)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',
                           item_name = list(popular_df['item_name'].values),
                           frequency = list(popular_df['Frequency'].values),

                           )

@app.route('/recommend')
def recommend_ui():
    return render_template('recommend.html')
#
@app.route('/recommend_items',methods=['post'])
def recommend():
    item = request.form.get('user_input')
    index = np.where(pt.index == item)[0][0]
    similar_items = sorted(list(enumerate(similarity_scores[index])), key=lambda x: x[1], reverse=True)[1:6]
    list1=[]
    for i in similar_items:
        list1.append(pt.index[i[0]])
    print(list1)
    return render_template('recommend.html', data=list1)


if __name__ == '__main__':
    app.run(debug=True)