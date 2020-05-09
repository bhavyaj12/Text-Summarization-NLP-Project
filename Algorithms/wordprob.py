import nltk
import heapq
from nltk.corpus import stopwords

txt="Democracy isn’t taking over the world as many hoped. In many places, it seems to be in decline, and a group of scientists tasked with studying this decline says it’s because of a complicated series of interconnected feedback loops, such as rising inequality causing political polarization. At the end of the 20th century, political theorist Francis Fukuyama declared the “end of history.” People assumed democracy had won, but now authoritarianism and dictatorships are rising again. Human society is a complex web of connections, with any single event causing many different outcomes depending on many factors. Feedback loops often produce effects that spiral well beyond the original event that started the chain reaction, such as the popularly known “butterfly effect” in natural systems. Using complex systems analysis, scientists from the University of Bristol found five interconnected reasons behind the decline of democracies. In their study, published in the European Journal of Physics, they note that “many of these mechanisms are interconnected, meaning that their temporal and/or spatial dynamics are not separable but influence each other to a significant degree.” The economy, culture, politics, technology and everything else are all linked and influence each other, often in unpredictable ways. And like in natural systems, “The system may even transform itself into a completely different structure via its capacity to evolve.” First, there was feudalism, then there was mercantilism, and now there is capitalism."
sentence_list = nltk.sent_tokenize(txt)  

stpwrds = stopwords.words('english')

wordfreq = {}  
for word in nltk.word_tokenize(txt):  
    if word not in stpwrds:
        if word not in wordfreq.keys():
            wordfreq[word] = 1
        else:
            wordfreq[word] += 1

maxfreq = max(wordfreq.values())

for word in wordfreq.keys():  
    wordfreq[word] = (wordfreq[word]/maxfreq)

sentence_scores = {}  
for sent in sentence_list:  
    for word in nltk.word_tokenize(sent.lower()):
        if word in wordfreq.keys():
            if len(sent.split(' ')) < 30:
                if sent not in sentence_scores.keys():
                    sentence_scores[sent] = wordfreq[word]
                else:
                    sentence_scores[sent] += wordfreq[word]

summary_sentences = heapq.nlargest(5, sentence_scores, key=sentence_scores.get)

summary = ' '.join(summary_sentences)  
print(summary)

