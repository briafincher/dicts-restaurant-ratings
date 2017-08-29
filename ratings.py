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
import random


def get_user_input(scores):
    """Gives user options for restaurant rating program."""

    while True:
        print
        print "If you want to see restaurant ratings, type 'Ratings'."
        print "If you want to add a new restaurant, type 'New'."
        print "If you want to update a restaurant's rating, type 'Update'."
        print "If you want a recommendation, type 'Recommend'"
        print "If you wish to quit, type 'Quit'."
        print

        user_input = raw_input('> ')

        if user_input == 'Ratings':
            see_all_ratings(scores)
        elif user_input == 'New':
            new_restaurant = raw_input('restaurant name > ').capitalize()
            rate_new_restaurant(scores, new_restaurant)
        elif user_input == 'Update':
            restaurant = raw_input('Restaurant name > ').capitalize()
            rate_new_restaurant(scores, restaurant)
        elif user_input == 'Recommend':
            get_random_restaurant(scores)
        elif user_input == 'Quit':
            break
        else:
            print "That is not a valid command."


def see_all_ratings(scores):
    """"Prints out all restaurant ratings in alphabetical order."""

    for restaurant, score in sorted(scores.items()):
        print "{} is rated at {}.".format(restaurant, score)


def rate_new_restaurant(scores, restaurant):
    """Updates restaurant list with user submitted rating."""

    while True:
        new_restaurant_rating = int(raw_input('new score > '))
        if new_restaurant_rating <= 5:
            break
        print 'Restaurants can only be rated to 5'

    scores[restaurant] = new_restaurant_rating


def get_random_restaurant(scores):
    """Generates random restaurant recommendation and asks for new score."""

    recommendation = random.choice(scores.keys())

    print 'Restaurant: {}, Score: {}'.format(recommendation, scores[recommendation])

    rate_new_restaurant(scores, recommendation)


with open('scores.txt') as restaurant_scores:
    scores = {}
    for line in restaurant_scores:
        line = line.strip().split(':')
        scores[line[0]] = line[1]

    get_user_input(scores)
