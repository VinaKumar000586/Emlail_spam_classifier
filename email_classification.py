# -*- coding: utf-8 -*-
"""Email_Classification.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1MNqhuQTTbXy5Bm4fGg6-G4eB_K95MCPo
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import nltk
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import VotingClassifier,GradientBoostingClassifier

nltk.download('punkt_tab')

df = pd.read_csv('/content/email.csv')

df.head()

df.isnull().sum()

df.dropna(inplace=True)

df.duplicated().sum()

df.drop_duplicates(inplace=True)



df.rename(columns={'Category':'label','Message':'text'},inplace=True)

df.shape

from sklearn.preprocessing import LabelEncoder
encoding = LabelEncoder()
df['label'] = encoding.fit_transform(df['label'])



"""#***EDA***"""

df['label'].value_counts()

plt.pie(df['label'].value_counts(),labels=df['label'].value_counts().index,autopct = "%0.2f")

df['num_character'] = df['text'].apply(len)

df['num_word'] = df['text'].apply(lambda x: len(nltk.word_tokenize(x)))

df['num_setences'] = df['text'].apply(lambda x: len(nltk.sent_tokenize(x)))

df.head()

df.info()

df.describe()

df[df['label']==0][['num_character','num_word','num_setences']].describe()

df[df['label']==1][['num_character','num_word','num_setences']].describe()

df_numeric = df.select_dtypes(include=['number'])
sns.heatmap(df_numeric.corr(),annot=True)

sns.pairplot(df,hue='label')



"""## ***Data Preprocessing***"""

from nltk.corpus import stopwords
nltk.download('stopwords')

from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()

import string

def transformed_text(text):
  text = text.lower()
  text = nltk.word_tokenize(text)
  y = []
  for i in text:
    if i.isalnum():
      y.append(i)
  text = y[:]
  y.clear()
  for i in text:
    if i not in stopwords.words('english') and i not in string.punctuation:
      y.append(i)
  text = y[:]
  y.clear()

  for i in text:
    y.append(ps.stem(i))

  text = y[:]
  y.clear()

  return " ".join(text)

transformed_text('Hi My Name Is Vinay loved %% eg')



df['transformed_text'] = df['text'].apply(transformed_text)

from wordcloud import WordCloud
wc = WordCloud(width=500,height=500,min_font_size=10,background_color='white')

spam_wc = wc.generate(df[df['label']==1]['transformed_text'].str.cat(sep=" "))

plt.figure(figsize=(15,6))
plt.imshow(spam_wc)

ham_wc = wc.generate(df[df['label']==0]['transformed_text'].str.cat(sep=" "))

plt.figure(figsize=(15,6))
plt.imshow(ham_wc)

spam_corpus = []
for mess in df[df['label']==1]['transformed_text'].tolist():
  print(mess)
  for words in mess.split():
    spam_corpus.append(words)

from collections import Counter
sns.barplot(x = pd.DataFrame(Counter(spam_corpus).most_common(30))[0],y = pd.DataFrame(Counter(spam_corpus).most_common(30))[1])
plt.xticks(rotation='vertical')
plt.show()

from collections import Counter

ham_corpus = []
for mess in df[df['label']==0]['transformed_text'].tolist():
  print(mess)
  for words in mess.split():
    ham_corpus.append(words)

sns.barplot(x = pd.DataFrame(Counter(ham_corpus).most_common(30))[0],y = pd.DataFrame(Counter(ham_corpus).most_common(30))[1])
plt.xticks(rotation='vertical')
plt.show()



"""# ***##Model Building***"""









from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer
cv = CountVectorizer()
tidf = TfidfVectorizer(max_features=3000)
from sklearn.naive_bayes import MultinomialNB,BernoulliNB,GaussianNB
from sklearn.metrics import accuracy_score,confusion_matrix,precision_score

X = cv.fit_transform(df['transformed_text']).toarray()

y = df['label'].values

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=2)

gnb = GaussianNB()
mlb = MultinomialNB()
bnb = BernoulliNB()

"""#making the different naive Bayes model for checking in which model the accuracy and precision_score is best"""

gnb.fit(X_train,y_train)
y_pred1 = gnb.predict(X_test)
print(accuracy_score(y_test,y_pred1))
print(confusion_matrix(y_test,y_pred1))
print(precision_score(y_test,y_pred1))



bnb.fit(X_train,y_train)
y_pred3 = bnb.predict(X_test)
print(accuracy_score(y_test,y_pred3))
print(confusion_matrix(y_test,y_pred3))
print(precision_score(y_test,y_pred3))



"""# using tfidf over CountVectorizer,TfidfVectorizer for checking is model performe better or not

"""

tidf = TfidfVectorizer(max_features=3000)

X_ = tidf.fit_transform(df['transformed_text']).toarray()

X_train_,X_test_,y_train_,y_test_=train_test_split(X_,y,test_size=0.2,random_state=2)

gnb.fit(X_train_,y_train_)
y_pred1_ = gnb.predict(X_test_)
print(accuracy_score(y_test_,y_pred1_))
print(confusion_matrix(y_test_,y_pred1_))
print(precision_score(y_test_,y_pred1_,average='macro'))

#best model_performing
mlb.fit(X_train_,y_train_)
y_pred2_ = mlb.predict(X_test_)
print(accuracy_score(y_test_,y_pred2_))
print(confusion_matrix(y_test_,y_pred2_))
print(precision_score(y_test_,y_pred2_))

bnb.fit(X_train_,y_train_)
y_pred3_ = bnb.predict(X_test_)
print(accuracy_score(y_test_,y_pred3_))
print(confusion_matrix(y_test_,y_pred3_))
print(precision_score(y_test_,y_pred3_))

##here we can clearly see the precision score are increase in MultinomialNB and also increas in accuracy for now this model the best model

#checking the other model

from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.naive_bayes import MultinomialNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier, GradientBoostingClassifier
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.ensemble import VotingClassifier

lG = LogisticRegression(solver='liblinear',penalty='l1' )
dt = DecisionTreeClassifier()
rf = RandomForestClassifier(n_estimators=150,random_state=2)
knn = KNeighborsClassifier()
svm = SVC(kernel='sigmoid',gamma= 0.1 )
nb = MultinomialNB()
ad = AdaBoostClassifier(n_estimators=60,random_state=2)
gb = GradientBoostingClassifier(n_estimators=50,random_state=2)
ex = ExtraTreesClassifier(n_estimators=60,random_state=2)

clf = {'lg':lG,'dt':dt,'rf':rf,'knn':knn,'svm':svm,'nb':nb,'ad':ad,'gb':gb,'ex':ex}
type(clf)

from sklearn.metrics import accuracy_score, confusion_matrix, precision_score

def model_train(clf, X_train_, y_train_, X_test_, y_test_):
    clf.fit(X_train_, y_train_)
    y_pred = clf.predict(X_test_)

    accuracy = accuracy_score(y_test_, y_pred)
    precision = precision_score(y_test_, y_pred)  # Specify for multiclass

    return accuracy, precision

# Ensure `lG` (classifier) is defined properly before calling model_train

model_train(lG, X_train, y_train, X_test, y_test)



accuracy_scores = []
precision_scores = []

for name, Clf in clf.items():
    current_accuracy,current_precision = model_train(Clf, X_train_, y_train_, X_test_, y_test_)

    print(f"For {name}:")
    print(f"Accuracy - {current_accuracy}")
    print(f"Precision - {current_precision}")

    accuracy_scores.append(current_accuracy)
    precision_scores.append(current_precision)
model = pd.DataFrame({'Accuracy':accuracy_scores,'Precision':precision_scores},index=clf.keys())





vc = VotingClassifier(estimators=[('rf',rf),('knn',knn),('ex',ex),])

vc.fit(X_train_,y_train_)

y_pred_ = vc.predict(X_test_)
print(accuracy_score(y_test_,y_pred_))
print(confusion_matrix(y_test_,y_pred_))
print(precision_score(y_test_,y_pred_))

import pickle

pickle.dump(tidf,open('vectorizer.pkl','wb'))
pickle.dump(mlb,open('model.pkl','wb'))

d = df[df['label']==1]['text']
d.iloc[0]