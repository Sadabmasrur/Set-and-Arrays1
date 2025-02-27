setx={"green","yellow"}
sety={"blue","yellow"}

print("Original set element: ")
print(setx)
print(sety)

print("\nItersection of two set: ")
setz=setx.intersection(sety)
print(setz)

print("\nUnion pf two set: ")
setz=setx.union(sety)
print(setz)

print("\nDifference of two set: ")
setz=setx.difference(sety)
print(setz)

print("\nSymmetric difference of two set: ")
setz=setx.symmetric_difference(sety)
print(setz)