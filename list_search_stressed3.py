# find repeated strings

import random

list = []
for i in range(1000):
    list.append(random.randint(1,10))
#print(list)

mylist = list

#mylist = [4,7,1,1,5,2,7,9,4,7,2,6,8,6,1,5,4,7,2]


searchlen = int(input('INT what is your query sample size?'))
short_search = 3
mid_search = 10
long_search = 20

w_list = mylist[:]
w_list_rev = mylist[:]
w_list_rev = w_list_rev[::-1]
query = w_list_rev[0:searchlen]
#recent = w_list_rev[0:2]
nw_list_rev = w_list_rev[searchlen:]
print(query)
print(nw_list_rev)

#matchlist = [matchlen,data,location]
matches = []
matchlist = []

# count of matches
mcount = 0
mlen = 0
# place in list
lcount = 0

for i in nw_list_rev:
    # place in query
    qcount = 0
    #print(str(i) + ' & ' + str(query[qcount]) + str(query[0]))
    #print('--')
    lcount += 1

    tmatch = []

    for g in query:
        if g == nw_list_rev[(lcount - 1) + qcount]:
            tmatch.append(g)
            qcount += 1
        qcount = 0


    mlen = len(tmatch)
    matches.append(tmatch)
        #tmatch = []
    matches.append(mlen)
    matches.append(lcount - 1)
    matchlist.append(matches)
    matches = []
print(matchlist)
#print(matchlist)
