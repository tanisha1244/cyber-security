def rev_sentence(sentence):

    words = sentence.split(' ')


    reverse_sentence = ' '.join(reversed(words))


    return reverse_sentence

a = input()
print ( "reversed_words","(",a,")","-->",rev_sentence(a))
