from collector.rail import Rail

r = Rail()
while True:
    print "1 : Goto Home"
    print "2 : Goto Waiting for sort position"
    print "3 : Goto Away (Dump)"
    c = int(raw_input("your choice?"))

    if c ==1:
        print "going home"
        import pdb
        pdb.set_trace()
        r.slide_to_home()
    if c == 2:
        print "going wait"
        r.slide_to_wait_for_sorting_position()
    if c == 3:
        print "going dump"
        r.slide_to_away()

