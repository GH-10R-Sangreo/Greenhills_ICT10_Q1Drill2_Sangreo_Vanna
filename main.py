from js import document

def generating_messages(event):
    name = document.getElementById("name").value
    age = document.getElementById("age").value
    school = document.getElementById("school").value
    document.getElementById("output").innerText = f"{name}\'s age is {age} years old and {name}\'s school is {school}."

# assisted by Copilot!!!