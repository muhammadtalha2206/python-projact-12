# name=input("Enter your name.")
# marks=input("Enter your marks.")
# phone=input("Enter your phone.")
# tamples="the name of the student {} his marks are {} and phone number is {}."
# print(tamples.format(name, marks, phone))

# l=[str(i*7) for i in range(1, 11)]
# print(l)
# print("\n".join(l))

# l1=[1,2,3,4,5,6,7,8,9,5,4,55,65,75,90]
# a= filter (lambda a: a%5==0,l1)
# print(list(a))

# from functools import reduce
# l=[3,8,4,2,33,5]
# print(reduce(max, l))

from flask import Flask
app=Flask(__name__)
@app.route('/')
def hello_word():
    return 'Hello, Word!'
if __name__ =="__main__":
    app.run(debug=True)


