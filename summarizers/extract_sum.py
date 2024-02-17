
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest



def summarize(text, per):
    nlp = spacy.load('en_core_web_sm')
    doc= nlp(text)
    
    word_frequencies={}
    for word in doc:
        if word.text.lower() not in list(STOP_WORDS):
            if word.text.lower() not in punctuation:
                if word.text not in word_frequencies.keys():
                    word_frequencies[word.text] = 1
                else:
                    word_frequencies[word.text] += 1
    max_frequency=max(word_frequencies.values())
    for word in word_frequencies.keys():
        word_frequencies[word]=word_frequencies[word]/max_frequency
    sentence_tokens= [sent for sent in doc.sents]
    sentence_scores = {}
    for sent in sentence_tokens:
        for word in sent:
            if word.text.lower() in word_frequencies.keys():
                if sent not in sentence_scores.keys():                            
                    sentence_scores[sent]=word_frequencies[word.text.lower()]
                else:
                    sentence_scores[sent]+=word_frequencies[word.text.lower()]
    select_length=int(len(sentence_tokens)*per)
    summary=nlargest(select_length, sentence_scores,key=sentence_scores.get)
    final_summary=[word.text for word in summary]
    summary=''.join(final_summary)
    return summary

text = """
J. Robert Oppenheimer (1904-1967) was an American theoretical physicist. 
During the Manhattan Project, Oppenheimer was director of the Los Alamos Laboratory and responsible for the research and design of an atomic bomb. 
He is often known as the
“father of the atomic bomb.”By the time the Manhattan Project was launched in the
fall of 1942, Oppenheimer was already considered an exceptional theoretical
physicist and had become deeply involved in exploring the possibility of an atomic
bomb. Throughout the previous year he had been doing research on fast neutrons,
calculating how much material might be needed for a bomb and how efficient it might
be. Although Oppenheimer had little managerial experience and some troublesome
past associations with Communist causes, General Leslie Groves recognized his
exceptional scientific brilliance. Less than three years after Groves selected
Oppenheimer to direct weapons development, the United States dropped two atomic
bombs on Japan. As director of the Los Alamos Laboratory, Oppenheimer proved to
be an extraordinary choice.
"""


# print(summarize(text,0.5))