http_status = 400

match http_status:
    case 200 | 201:
        print("Success")
    case 400:
        print("Not Found")
    case 500 | 501:
        print("Server Error")
    case _:
        print("Unknown")
        
listo = ["a", "b", "c", "d"]
for x, n in enumerate(listo):
    print(x,n)

i = 0
while i < 10:
    print(i)
    i+=1