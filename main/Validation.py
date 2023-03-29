#validation fields
min_Width = 111
min_Height = 111

#validating if its a vehicle to minimise errors
        if not ((w >= min_Width) and (h >= min_Height)):
            continue
