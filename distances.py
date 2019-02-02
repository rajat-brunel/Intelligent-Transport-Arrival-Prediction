def distances(cur_stop, next_Stop):
    if cur_stop == 'Uxbridge Station' and next_Stop == 'Uxbridge High Street':
        dist = 280
    elif cur_stop == 'Uxbridge High Street' and next_Stop == 'Crown Walk':
        dist = 500
    elif cur_stop == 'Crown Walk' and next_Stop == 'Vine Street':
        dist = 380
    elif cur_stop == 'Vine Street' and next_Stop == "St Andrew's Church":
        dist = 470
    elif cur_stop == "St Andrew's Church" and next_Stop == "Manor Waye":
        dist = 225
    elif cur_stop == "Manor Waye" and next_Stop == "Uxbridge High School":
        dist = 620
    elif cur_stop == "Uxbridge High School" and next_Stop == "Brunel University":
        dist = 590
    elif cur_stop == "Brunel University" and next_Stop == "Huxley Close":
        dist = 400
    elif cur_stop == "Huxley Close" and next_Stop == "St Lawrence Church":
        dist = 150
    elif cur_stop == "St Lawrence Church" and next_Stop == "Pield Heath":
        dist = 310
    elif cur_stop == "Pield Heath" and next_Stop == "Peel Way":
        dist = 260
    elif cur_stop == "Peel Way" and next_Stop == "Hillingdon Hospital":
        dist = 390
    elif cur_stop == "Hillingdon Hospital" and next_Stop == "Colham Road":
        dist = 210
    elif cur_stop == "Colham Road" and next_Stop == "Violet Avenue":
        dist = 525
    elif cur_stop == "Violet Avenue" and next_Stop == "Apple Tree Avenue":
        dist = 1000
    elif cur_stop == "Apple Tree Avenue" and next_Stop == "Otterfield Road":
        dist = 530
    elif cur_stop == "Otterfield Road" and next_Stop == "Yiewsley Library":
        dist = 375
    elif cur_stop == "Yiewsley Library" and next_Stop == "Yiewsley High Street":
        dist = 315
    elif cur_stop == "Yiewsley High Street" and next_Stop == "West Drayton Station":
        dist = 420
    elif cur_stop == "West Drayton Station" and next_Stop == "Ferrers Avenue":
        dist = 275
    elif cur_stop == "Ferrers Avenue" and next_Stop == "Swan Road":
        dist = 435
    elif cur_stop == "Swan Road" and next_Stop == "The Green":
        dist = 325
    elif cur_stop == "The Green" and next_Stop == "Mill Road":
        dist = 180
    elif cur_stop == "Mill Road" and next_Stop == "Roseary Close":
        dist = 445
    elif cur_stop == "Roseary Close" and next_Stop == "Magnolia Street":
        dist = 130
    elif cur_stop == "Magnolia Street" and next_Stop == "Great Benty":
        dist = 175
    elif cur_stop == "Great Benty" and next_Stop == "Laurel Lane Primary School":
        dist = 225
    elif cur_stop == "Laurel Lane Primary School" and next_Stop == "Berberis Walk":
        dist = 325
    elif cur_stop == "Berberis Walk" and next_Stop == "Harmondsworth Road":
        dist = 325
    elif cur_stop == "Harmondsworth Road" and next_Stop == "Harmondsworth Lane":
        dist = 930
    elif cur_stop == "Harmondsworth Lane" and next_Stop == "Candover Close":
        dist = 500
    elif cur_stop == "Candover Close" and next_Stop == "Skyport Drive":
        dist = 375
    elif cur_stop == "Skyport Drive" and next_Stop == "Pinglestone Close":
        dist = 240
    elif cur_stop == "Pinglestone Close" and next_Stop == "Compass Centre":
        dist = 450
    elif cur_stop == "Compass Centre" and next_Stop == "Newport Road":
        dist = 415
    elif cur_stop == "Newport Road" and next_Stop == "Sipson Way / Blunts Avenue":
        dist = 480
    elif cur_stop == "Sipson Way / Blunts Avenue" and next_Stop == "Heathrow Central Bus Station":
        dist = 1730
    else:
        dist = 0
    return dist


def distances_inbound(cur_stop, next_stop):
    if cur_stop == 'Crown Walk' and next_stop == "Belmont Road":
        dist = 715
    elif cur_stop == 'Civic Centre' and next_stop == "Crown Walk":
        dist = 640
    elif cur_stop == "St Andrew's Church" and next_stop == "Civic Centre":
        dist = 280
    elif cur_stop == "Manor Waye" and next_stop == "St Andrew's Church":
        dist = 305
    elif cur_stop == "Uxbridge High School" and next_stop == "Manor Waye":
        dist = 550
    elif cur_stop == "Villier Street" and next_stop == "Uxbridge High School":
        dist = 225
    elif cur_stop == "Brunel University" and next_stop == "Villier Street":
        dist = 300
    elif cur_stop == "Huxley Close" and next_stop == "Brunel University":
        dist = 530
    elif cur_stop == "St Laurence Church" and next_stop == "Huxley Close":
        dist = 155
    elif cur_stop == "Peel Way" and next_stop == "St Laurence Church":
        dist = 535
    elif cur_stop == "Hillingdon Hospital" and next_stop == "Peel Way":
        dist = 385
    elif cur_stop == "Colham Road" and next_stop == "Hillingdon Hospital":
        dist = 320
    elif cur_stop == "Violet Avenue" and next_stop == "Colham Road":
        dist = 345
    elif cur_stop == "Apple Tree Avenue" and next_stop == "Violet Avenue":
        dist = 960
    elif cur_stop == "Milburn Drive" and next_stop == "Apple Tree Avenue":
        dist = 450
    elif cur_stop == "Yiewsley Library" and next_stop == "Milburn Drive":
        dist = 365
    elif cur_stop == "Yiewsley High Street" and next_stop == "Yiewsley Library":
        dist = 375
    elif cur_stop == "West Drayton Station" and next_stop == "Yiewsley High Street":
        dist = 340
    elif cur_stop == "Ferrers Avenue" and next_stop == "West Drayton Station":
        dist = 405
    elif cur_stop == "Swan Road" and next_stop == "Ferrers Avenue":
        dist = 410
    elif cur_stop == "The Green" and next_stop == "Swan Road":
        dist = 340
    elif cur_stop == "Mill Road" and next_stop == "The Green":
        dist = 315
    elif cur_stop == "Roseary Close" and next_stop == "Mill Road":
        dist = 330
    elif cur_stop == "Magnolia Street" and next_stop == "Roseary Close":
        dist = 220
    elif cur_stop == "Great Benty" and next_stop == "Magnolia Street":
        dist = 100
    elif cur_stop == "Laurel Lane Primary School" and next_stop == "Great Benty":
        dist = 190
    elif cur_stop == "Berberis Walk" and next_stop == "Laurel Lane Primary School":
        dist = 320
    elif cur_stop == "Harmondsworth Road" and next_stop == "Berberis Walk":
        dist = 265
    elif cur_stop == "Harmondsworth Lane" and next_stop == "Harmondsworth Road":
        dist = 1075
    elif cur_stop == "Candover Close" and next_stop == "Harmondsworth Lane":
        dist = 445
    elif cur_stop == "Skyport Drive" and next_stop == "Candover Close":
        dist = 390
    elif cur_stop == "Pinglestone Close" and next_stop == "Skyport Drive":
        dist = 165
    elif cur_stop == "Compass Centre" and next_stop == "Pinglestone Close":
        dist = 500
    elif cur_stop == "Bath Road / Newport Road" and next_stop == "Compass Centre":
        dist = 445
    elif cur_stop == "Newport Road" and next_stop == "Bath Road / Newport Road":
        dist = 425
    elif cur_stop == "Heathrow Central Bus Station" and next_stop == "Newport Road":
        dist = 1630
    else:
        dist = 0
    return dist


def dist_tube(cur_stop, next_stop):
    if cur_stop == 'Uxbridge Underground Station' and next_stop == "Hillingdon Underground Station":
        dist = 2140
    elif cur_stop == 'Hillingdon Underground Station' and next_stop == "Ickenham Underground Station":
        dist = 1120
    elif cur_stop == "Ickenham Underground Station" and next_stop == "Ruislip Underground Station":
        dist = 1780
    elif cur_stop == "Ruislip Underground Station" and next_stop == "Ruislip Manor Underground Station":
        dist = 630
    elif cur_stop == "Ruislip Manor Underground Station" and next_stop == "Eastcote Underground Station":
        dist = 1140
    elif cur_stop == "Eastcote Underground Station" and next_stop == "Rayners Lane Underground Station":
        dist = 1840
    elif cur_stop == 'Rayners Lane Underground Station' and next_stop == "West Harrow Underground Station":
        dist = 1120
    elif cur_stop == "West Harrow Underground Station" and next_stop == "Harrow-on-the-Hill Underground Station":
        dist = 1110
    elif cur_stop == "Harrow-on-the-Hill Underground Station" and next_stop == "Northwick Park Underground Station":
        dist = 1340
    elif cur_stop == "Northwick Park Underground Station" and next_stop == "Preston Road Underground Station":
        dist = 1750
    elif cur_stop == "Preston Road Underground Station" and next_stop == "Wembley Park Underground Station":
        dist = 1460
    elif cur_stop == "Wembley Park Underground Station" and next_stop == "Finchley Road Underground Station":
        dist = 7260
    elif cur_stop == 'Finchley Road Underground Station' and next_stop == "Baker Street Underground Station":
        dist = 3280
    elif cur_stop == "Baker Street Underground Station" and next_stop == "Great Portland Street Underground Station":
        dist = 950
    elif cur_stop == "Great Portland Street Underground Station" and next_stop == "Euston Square Underground Station":
        dist = 650
    elif cur_stop == "Euston Square Underground Station" and next_stop == "King's Cross St. Pancras Underground Station":
        dist = 930
    elif cur_stop == "King's Cross St. Pancras Underground Station" and next_stop == "Farringdon Underground Station":
        dist = 1830
    elif cur_stop == "Farringdon Underground Station" and next_stop == "Barbican Underground Station":
        dist = 525
    elif cur_stop == "Barbican Underground Station" and next_stop == "Moorgate Underground Station":
        dist = 670
    elif cur_stop == "Moorgate Underground Station" and next_stop == "Liverpool Street Underground Station":
        dist = 400
    elif cur_stop == "Liverpool Street Underground Station" and next_stop == "Aldgate Underground Station":
        dist = 640
    else:
        dist = 0
    return dist
