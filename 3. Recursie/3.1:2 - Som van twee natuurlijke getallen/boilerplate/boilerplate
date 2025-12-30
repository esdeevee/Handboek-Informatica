def aantal_manieren(n):
    if n <= 1:
	    # voor een trap met 0 of 1 trede is het probleem al opgelost
	    # er is maar 1 manier om een trap met 0 of 1 trede te beklimmen
	    return 1
    else:
	    # het aantal trappen is minstens 2
	    # we noteren het patroon dat we ingezien hadden
	    eturn aantal_manieren(n - 1) + aantal_manieren(n - 2)

print(aantal_manieren(0))
