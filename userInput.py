from emotions import create_feature, vectorizer, clf, emoji_dict

"""
t1 = "I don't know what to do after my father passed away yesterday"
t2 = "I do not feel that well today"
t3 = "My dog died yesterday"
t4 = "I don't love you anymore..!"

texts = [t1, t2, t3, t4]
for text in texts: 
    features = create_feature(text, nrange=(1, 4))
    features = vectorizer.transform(features)
    prediction = clf.predict(features)[0]
    print( text,emoji_dict[prediction])
"""

while (True):
    textInput = input("")

    if(textInput == "0"):
        break

    features = create_feature(textInput)
    features = vectorizer.transform(features)
    prediction = clf.predict(features)[0]
    print(textInput, emoji_dict[prediction])
    print("\n")