# Dict
# Key and value
# name -> "Pramod"

student_info = {
    "name": "pramod",
    "age" : 65,
    "address" : "KA"
}
print(student_info)
print(student_info["name"])
print(student_info["age"])
print(student_info["address"])

student_info["age"] = 100
print(student_info)

student_info = dict(name="pramod", age= 67, address = "KA")
# A dictionary is an unordered collection of data

student_info1 = {
    "name": "pramod",
    "age" : 65,
    "address" : {
        "home_address" : "ND",
        "office_address" :"KA"
    }
}
student_info2 = {
    "name": "amit",
    "age" : 67,
    "address" :{
        "home_address" : "Goa",
        "office_address" : "KA"
    }
}
student_list = [student_info1,student_info2]
print(student_list)