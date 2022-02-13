import random

import pandas as pd
from nrclex import NRCLex

text = ['dejected', 'depressed', 'anxious', 'nervous', 'enthusiastic', 'excited', 'calm', 'at ease']
for i in range(len(text)):
    # Create object
    emotion = NRCLex(text[i])
    # Classify emotion
    print('\n\n', text[i], ': ', emotion.top_emotions)

df = pd.read_csv('quotes.csv')
print(df.head(5))
df['quote'] = df['quote'].astype(str)
df['emotions'] = df['quote'].apply(lambda x: NRCLex(x).top_emotions)
print(df.head)
print(df.describe)

df = df.loc[1:100, ['quote', 'author', 'category', 'emotions']]
print(df.describe)

used_quotes = []

trust_quotes = []
joy_quotes = []
anticipation_quotes = []
fear_quotes = []
sadness_quotes = []
random_quotes = []
top_emotion = []

for q in df['quote']:
    if len(NRCLex(q).top_emotions) > 1:
        random_choice = random.choice(NRCLex(q).top_emotions)
        top_emotion.append(random_choice)
    elif len(NRCLex(q).top_emotions) == 1:
        top_emo = NRCLex(q).top_emotions
        top_emotion.append(top_emo)
    else:
        NA_emotion = 'NaN'
        top_emotion.append(NA_emotion)

print(top_emotion)
type(top_emotion)
type(top_emotion[0])
output = [tuple(j for j in i if isinstance(j, str)) for i in top_emotion]
print(output)

df['output'] = output
print(df.head)

type(df['output'])
print(df['output'].head)
df['output'] = df['output'].astype(str)

df['output'] = df['output'].str.replace(',','')
df['output'] = df['output'].str.replace('(','')
df['output'] = df['output'].str.replace(')','')
df['output'] = df['output'].str.replace("'",'')

for i, row in df.iterrows():
    index = i-1
    content = df['output'].iloc[index].strip('\'')
    if content == 'trust':
        quo = df['quote'].iloc[index]
        trust_quotes.append(quo)
    elif content == 'joy':
        qua = df['quote'].iloc[index]
        joy_quotes.append(qua)
    elif content == 'anticipation':
        qui = df['quote'].iloc[index]
        anticipation_quotes.append(qui)
    elif content == 'fear':
        que = df['quote'].iloc[index]
        fear_quotes.append(que)
    elif content == 'sadness':
        qu = df['quote'].iloc[index]
        sadness_quotes.append(qu)
    else:
        quu = df['quote'].iloc[index]
        random_quotes.append(quu)

print(random_quotes)
print(joy_quotes)

# moods go from 0-100
moods = ['depressed', 'depressed', 'anxious', 'enthusiastic', 'excited', 'excited', 'excited', 'at ease']

for mo in moods:
    if mo == 'at ease':
        for trust in trust_quotes:
            if trust != used_quotes:
                print(trust_quotes[trust])
                used_quotes.append(trust)
            elif trust == used_quotes:
                trust = trust + 1
                print(trust_quotes[trust])
                used_quotes.append(trust)
    elif mo == 'calm':
        for trust in trust_quotes:
            if trust != used_quotes:
                print(trust_quotes[trust])
                used_quotes.append(trust)
            elif trust == used_quotes:
                trust = trust + 1
                print(trust_quotes[trust])
                used_quotes.append(trust)
    elif mo == 'excited':
        for joy in joy_quotes:
            if joy != used_quotes:
                print(joy_quotes[joy])
                used_quotes.append(joy)
            elif joy == used_quotes:
                joy = joy + 1
                print(joy_quotes[joy])
                used_quotes.append(joy)
    elif mo == 'enthusiastic':
        for joy in joy_quotes:
            if joy != used_quotes:
                print(joy_quotes[joy])
                used_quotes.append(joy)
            elif joy == used_quotes:
                joy = joy + 1
                print(joy_quotes[joy])
                used_quotes.append(joy)
    elif mo == 'nervous':
        for anticipation in anticipation_quotes:
            if anticipation != used_quotes:
                print(anticipation_quotes[anticipation])
                used_quotes.append(anticipation)
            elif anticipation == used_quotes:
                anticipation = anticipation + 1
                print(anticipation_quotes[anticipation])
                used_quotes.append(anticipation)
    elif mo == 'anxious':
        for fear in fear_quotes:
            if fear != used_quotes:
                print(fear_quotes[fear])
                used_quotes.append(fear)
            elif fear == used_quotes:
                fear = fear + 1
                print(fear_quotes[fear])
                used_quotes.append(fear)
    elif mo == 'depressed':
        for sadness in sadness_quotes:
            if sadness != used_quotes:
                print(sadness_quotes[sadness])
                used_quotes.append(sadness)
            elif sadness == used_quotes:
                sadness = sadness + 1
                print(sadness_quotes[sadness])
                used_quotes.append(sadness)
    elif mo == 'dejected':
        for sadness in sadness_quotes:
            if sadness != used_quotes:
                print(sadness_quotes[sadness])
                used_quotes.append(sadness)
            elif sadness == used_quotes:
                sadness = sadness + 1
                print(sadness_quotes[sadness])
                used_quotes.append(sadness)

# for i in list_of_quotes:
    # if i != used_quotes:
        # print(i)
        # used_quotes.append(i)
    # elif i == list_of_quotes:
        # i = i + 1
        # print(i)
        # used_quotes.append(i)

# mood['depressed'] == mood['sadness']
# mood['dejected'] == mood['sadness']
# mood['anxious'] == mood['fear']
# mood['nervous'] == mood['anticipation']
# mood['enthusiastic'] == mood['joy']
# mood['excited'] == mood['joy']
# mood['calm'] == mood['trust']
# mood['at ease'] == mood['trust']
# text_object = NRCLex('quotes-EN.json')

# emotion = []
# for i in range(len(df)):
    # emotions = NRCLex(df['quote'][i])
# df['emotion'][i] = emotion
# text_object.words
# text_object.affect_dict
# text_object = NRCLex(lexicon_file='quotes-EN.json')
# text_object.load_raw_text('quotes-EN.json')
# for i in range(len(text_object)):
# creating objects
# emotion = NRCLex(text_object[i])
# Classify emotion
# print('\n\n', text_object[i], ': ', emotion.top_emotions)

# for m in mood:
    # if m.top_emotions == 'depressed':
        # moods.append('depressed')
    # elif m.top_emotions == 'anxious':
        # moods.append('anxious')
    # elif m.top_emotions == 'nervous':
        # moods.append('nervous')
    # elif m.top_emotions == 'enthusiastic':
        # moods.append('enthusiastic')
    # elif m.top_emotions == 'excited':
        # moods.append('excited')
    # elif m.top_emotions == 'calm':
        # moods.append('calm')
    # elif m.top_emotions == 'at ease':
        # moods.append('at ease')
    # elif m.top_emotions == 'dejected':
        # moods.append('dejected')

