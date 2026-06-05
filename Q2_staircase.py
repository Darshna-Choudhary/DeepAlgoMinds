def staircase(n):
    for i in range(n):
        s1 = " " * (n-1-i)
        print(s1, end = "")
        s = "#" * (i+1)
        print(s)

n = 4
staircase(n)
# Output:
#       #
#      ##
#     ###
#    ####
