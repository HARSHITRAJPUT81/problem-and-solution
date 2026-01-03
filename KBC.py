questions = [
    [
      "Number of primitive data types in Java are?",  
      "6"   "8"   "7"   "5", 
      2
    ],
    [
      "Which statement terminates the outer loop in a nested loop structure?",
      "a.break"     "b.continue"     "c.return"     "d.exit",
      1 
    ],
    [
        "How is dependency injection achieved in Java frameworks like Spring?",
        "a.Inheritance"         
        "b. Annotations and XML configuration"
        "c.Threading"              
        "d. Interface implementation",
        2
        
    ],
    [
        "Which keyword ensures no other thread accesses a synchronized method simultaneously?",
        "a.synchronized"
        "b. private"
        "c. volatile"
        "d.transient",
        1
    ],
    [
        "What is the process of defining a method in a subclass with the same name and type signature as a method in its superclass?",  
        "A.Method overloading" 
        "B.Method overriding"  
        "C.Method hiding"       
        "D.None of the mentioned",
        2
           
    ],
    [
      "Number of primitive data types in Java are?",  
      "A.6"   "B. 8"   "C. 7"   "D. 5",
      2
    ],
    [
      "Number of primitive data types in Java are?",  
      "A. 6"   "B. 8"   "C. 7"   "D. 5", 
      2
    ],
    [
      "Number of primitive data types in Java are?",  
      "A. 6"   "B. 8"   "C. 7"   "D. 5",
      2
    ],
    [
      "Number of primitive data types in Java are?",  
      "A. 6"   "B. 8"   "C. 7"   "D. 5", 
      2
    ]

]
levels = [1000,2000,3000,5000,10000,20000,40000,80000,160000]
money = 0
for i in range(len(questions)):
    question = questions[i]
    print(f"\nQuestion for Rs.{levels[i]}")
    print(question[0])

    print(f"1. {question[1]}")   
    print(f"2. {question[2]}")
    print(f"3. {question[3]}")  
    print(f"4. {question[4]}")

    reply = int(input("Enter your answer(1-4):"))
    if(reply == questions[5]):
      print(f"Correct answer!,you have won Rs.{levels[i]}")
      money = levels[i]
    else:
      print("Wrong answer!")
      break

print(f"n\Total money won:Rs.{money}")

questions = [
    ["Number of primitive data types in Java are?",
     "6", "8", "7", "5", 2],

    ["Which statement terminates the outer loop?",
     "break", "continue", "return", "exit", 1],

    ["How is dependency injection achieved in Spring?",
     "Inheritance", "Annotations and XML configuration",
     "Threading", "Interface implementation", 2],

    ["Which keyword ensures thread safety?",
     "synchronized", "private", "volatile", "transient", 1],

    ["Method with same name and signature in subclass is called?",
     "Method overloading", "Method overriding",
     "Method hiding", "None", 2]
]

levels = [1000, 2000, 3000, 5000, 10000]
money = 0

for i in range(len(questions)):
    q = questions[i]
    print(f"\nQuestion for Rs.{levels[i]}")
    print(q[0])
    print(f"1. {q[1]}")
    print(f"2. {q[2]}")
    print(f"3. {q[3]}")
    print(f"4. {q[4]}")

    reply = int(input("Enter your answer (1-4): or 0 to quit "))
    if (reply == 0):
        money = levels[i-1]
        break

    if reply == q[5]:
        print("Correct Answer ✅")
        money = levels[i]
    else:
        print("Wrong Answer ❌")
        break

print(f"\nTotal money won: Rs.{money}")

