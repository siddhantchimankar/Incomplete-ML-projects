import spacy

nlp = spacy.load('en_core_web_sm')

introText = ('Note that custom_ellipsis_sentences contain three sentences, whereas ellipsis_sentences contains two sentences. These sentences are still obtained via the sents attribute, as you saw before.')

introDoc = nlp(introText)

sentences = list(introDoc.sents)

for s in sentences:
    print(s)
