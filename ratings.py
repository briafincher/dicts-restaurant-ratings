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

with open('scores.txt') as restaurant_scores:
    scores = {}
    for line in restaurant_scores:
        line = line.strip().split(':')
        scores[line[0]] = line[1]

for restaurant, score in sorted(scores.items()):
    print "{} is rated at {}.".format(restaurant, score)
