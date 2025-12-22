letter = "Hey my name is {} and I am from {}"
name = "Harshit"
country = "India"
print(letter.format(name,country))

          #OR

letter = "Hey my name is {1} and I am from {0}"
name = "Harshit"
country = "India"
print(letter.format(name,country))

            #OR

print(f"Hey my name is {name} and I am from {country}")


price = 49.0988
txt = f"For only {price:.3f} dollars!"
print(txt)

              #OR

txt = "For only {price:.2f} dollars!"
print(txt.format(price=49.0988))



print(type(f"{2*30}"))


#If we want to print the output  like {name}and {country}, so we can use the {{name}} and {{country}}.
letter = "Hey my name is {1} and I am from {0}"
name = "Harshit"
country = "India"
print(f"Hey my name is {{name}} and I am from {{country}}")