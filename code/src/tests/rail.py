from collector.rail import Rail

r = Rail()
while True:
    print "1 : Goto Home"
    print "2 : Goto Waiting for sort position"
    print "3 : Goto Away (Dump)"
    c = int(raw_input("your choice?"))

    if c ==1:
        r.slide_to_home()
    elif c == 2:
        r.slide_to_wait_for_sorting_position()
    elif c == 3:
        r.slide_to_away()

