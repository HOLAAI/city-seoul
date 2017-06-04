def print_matches(matchtext):
    print "Looking for", matchtext
    print "Looking forqqqq", matchtext
    while True:
        line = (yield)
        if matchtext in line:
            print line



matcher = print_matches("python")
#matcher.next()
#matcher.send("py")