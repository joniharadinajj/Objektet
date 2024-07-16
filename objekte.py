person ={
    "Emri" : "Joni",
    "Mbiemri" : "Haradinaj",
    "Shkolla" : "jCoders",
    "Titulli" : "Student",
    "Mosha" : 17
}

emri = person["Emri"]
print(emri)

x = person.get("Emri")
print(x)

person["Mosha"] = 18
print(person)
'''
for i in person.values():
    print(i)
'''
for i in person:
    print(person[i])

if "Kompania" in person:
    print("Po eshte ne objekt")
else:
    print("JO nuk eshte")
    