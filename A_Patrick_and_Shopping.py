d1, d2, d3 = map(int, input().split())

# d1 road between his house and the first shop 
# d2 meter between his house and the second shop
# d3 directly connecting these two shops to each other.


dist1 = d1 + d1 + d2 + d2 # shop -> home -> shop2 -> home
dist2 = d1 + d3 + d2 # shop -> shop2 -> home
dist3 = d1 + d3 + d3 + d1 #shop -> shop2 -> shop -> home
dist4 = d2 + d3 + d3 + d2 #shop2 -> shop -> shop2 -> home

print(min([dist1, dist2, dist3, dist4]))