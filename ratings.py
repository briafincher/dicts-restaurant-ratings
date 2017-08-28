"""Restaurant rating lister."""

# open txt file
# create empty dictionary
# loop through each line
    # split each line with ':'
    # line[0] is key
    # line[1] is value
# iterate through dictionary using
# k in sorted(dictionary.items):
    # print
# format into correct string


def see_all_ratings(scores):
    """"Prints out all restaurant ratings in alphabetical order"""
    for restaurant, score in sorted(scores.items()):
        print "{} is rated at {}.".format(restaurant, score)


def rate_new_restaurant(scores):
    new_restaurant = raw_input('restaurant name > ').capitalize()

    while True:
        new_restaurant_rating = int(raw_input('score > '))
        if new_restaurant_rating <= 5:
            break
        print 'Restaurants can only be rated to 5'

    scores[new_restaurant] = new_restaurant_rating


with open('scores.txt') as restaurant_scores:
    scores = {}
    for line in restaurant_scores:
        line = line.strip().split(':')
        scores[line[0]] = line[1]

    while True:
        print
        print "If you want to see restaurant ratings, type 'Ratings'."
        print "If you want to add a new restaurant, type 'New'."
        print "If you wish to quit, type 'Quit'."
        print

        user_input = raw_input('> ')

        if user_input == 'Ratings':
            see_all_ratings(scores)
        elif user_input == 'New':
            rate_new_restaurant(scores)
        elif user_input == 'Quit':
            break
        else:
            print "That is not a valid command."
