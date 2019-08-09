


s = ['aaa', 'bbb', 'cccc']


def f(word):
    return word.capitalize() + '!'


def edit_story(words, func):
    for word in words:
        print(func(word))


edit_story(s, f)

# Второй вариант без функции f, она дописывается в вызов функции Edit_story:

edit_story(s, lambda word: word.capitalize() + "!")
