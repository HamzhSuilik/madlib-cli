import re

def get_story_text ():
    with open("./assets/story.txt", "r") as file:
        return file.read()
        

def get_word (text) :
    word = ''
    catch = 0
    for i in text :
        if catch == 0 :
            if i == '{' :
                catch = 1
        elif catch == 1 :
            if i == '}' :
                catch = 2
            else:
                word = word + i

    return word


def add_word (text,word):
    edit = ''
    catch = 0
    for i in text :
        if catch == 0 :
            if i == '{' :
                catch = 1
            else :
                edit = edit + i
        elif catch == 1 :
            if i == '}' :
                catch = 2
                edit = edit + word
        else :
            edit = edit + i
    return edit


def play ():
    print ('Welcome to the Madlib game')
    story = get_story_text ()
    while True :
        word = get_word (story)
        if word :
            user_input = input('write '+word+' :')
            story = add_word (story,user_input)
        else :
            break
    with open("./assets/story_2.txt", "w+") as f:
        f.write(story)
    print(story)

play()




