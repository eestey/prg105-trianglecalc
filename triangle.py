def is_triangle(s1, s2, s3):
    if (s1 > s2 + s3) or (s2 > s1 + s3) or (s3 > s1 + s2):
        print "No"
    else:
        print "Yes"


print ("Enter value for side 1:")
s1 = raw_input()
if s1 == '':
    s1 = "12"

print ("Enter value for side 2:")
s2 = raw_input
if s2 == '':
    s2 = "1"

print "Enter value for side 3:"
s3 = raw_input
if s3 == '':
    s3 = "1"

is_triangle(s1, s2, s3)
