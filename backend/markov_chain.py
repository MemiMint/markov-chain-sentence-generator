def markov_chain_sentence_generator(text):
    textArr = text.split() #split the string to convert it into an list
    markov_words = {} #initialize the dict containing the words of the text parameter

    for i in range(len(textArr)):
        word = textArr[i].lower().replace('/[\W_]/', "")

        if not markov_words.get(word):
            markov_words[word] = []
        
        if textArr[(i + 1) % len(textArr)]:
            markov_words[word].append(textArr[(i + 1) % len(textArr)].lower().replace('/[\W_]/', ""))
        
    return markov_words



