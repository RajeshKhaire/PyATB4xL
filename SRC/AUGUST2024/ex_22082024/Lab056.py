# Match statement
#switch in java
# match the op and execute
# python > 3.10

# MATCH VARIABLE:
# case pattern 1:
#   #code block
# case pattern 2:
#   #code block

# write a program to ask the user which browser he want to run automation
browser_name = input("Enter the name of the browser\n")
browser_name = browser_name.lower()
match browser_name:
    case "firefox":
        print("Execute the firefox code")
    case "chrome":
        print("Execute the chrome code")
    case "edge":
        print("Execute the firefox code")
    case "firefox":
        print("Execute the firefox code")
    case _:
        print("Browser Not Found")


# Match statement
#switch in java
# match the op and execute
# python > 3.10

# MATCH VARIABLE:
# case pattern 1:
#   #code block
# case pattern 2:
#   #code block

# write a program to ask the user which browser he want to run automation
browser_name = input("Enter the name of the browser\n")
browser_name = browser_name.lower()
match browser_name:
    case "firefox":
        if browser_name =="firefox":
            print("Hello Hello")
        print("Execute the firefox code")
    case "chrome":
        print("Execute the chrome code")
    case "edge":
        print("Execute the firefox code")
    case "firefox":
        print("Execute the firefox code")
    case _:
        print("Browser Not Found")