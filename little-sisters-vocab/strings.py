def add_prefix_un(word):
    return "un" + word
def make_word_groups(vocab_words):
    return (" :: " + vocab_words[0]).join(vocab_words)
def remove_suffix_ness(word):
    index = word.find("ness")
    revised_word = word[0:index]
    if revised_word[-1] == "i":
        return revised_word[0:-1] + "y"
    return word[0:index]
def noun_to_verb(sentence, index):
    extracted_word = sentence.split(" ")[index]
    if extracted_word[-1] == ".":
        return extracted_word[0:-1] + "en"
    return extracted_word + "en"
