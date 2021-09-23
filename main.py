# STACK DATA STRUCTURE using PYTHON
#*******************************#

#define a empty stack
stack = []

#push operation
def push():
  #check if stack is full
  if len(stack)==number:
    print("Stack Is FULL")
  else:
    element = input("Enter The Element: ")
    stack.append(element)
    print(stack)

#pop operation
def pop():
  #check if stack is empty
  if not stack:
    print("Stack Is Empty")
  else:
    element = stack.pop()
    print("Removed Element: ",element)
    print(stack)



#main function
number = int(input("Limit Of Stack:: "))

while True:
  print("Select the Operation: 1.push 2.pop 3.quit")
  choice= int(input())

  if choice==1:
    push()

  elif choice==2:
    pop()

  elif choice==3:
    break
  
  else:
    print("Enter a correct operation")