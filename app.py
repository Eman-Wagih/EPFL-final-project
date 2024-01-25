import flask
from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)

      
# cat class
class Cat: 
   def __init__ (self, name, age, breed, vaccinated, gender, image):
      self.name = name
      self.age = age
      self.breed = breed
      self.vaccinated = vaccinated
      self.gender = gender
      self.image = image
# to add the new instances to the database file 
   def add_new_cat(self):
      with open("Cat.json") as json_file:
         data = json.load(json_file)
         Kitty = data["cats"]
         temp = {"name":self.name,"age":self.age,"breed":self.breed,"gender": self.gender, "vaccinated":self.vaccinated, "image": self.image}
         Kitty.append(temp)
      with open("Cat.json", "w") as s:
         json.dump(data, s, indent=4)

# same as Cat class
class Dog: 
   def __init__ (self, name, age, breed, vaccinated, gender, image):
      self.name = name
      self.age = age
      self.breed = breed
      self.vaccinated = vaccinated
      self.gender = gender
      self.image = image
   def add_new_dog (self):
      with open("Dog.json") as json_file:
         data = json.load(json_file)
         dog = data["dogs"]
         temp = {"name":self.name,"age":self.age,"breed":self.breed,"gender": self.gender, "vaccinated":self.vaccinated, "image": self.image}
         dog.append(temp)
      with open("Dog.json", "w") as s:
         json.dump(data, s, indent=4)

# to creat new instances based on the user input 
def new_animal (type, name, age, breed, gender, vaccinated, image):
   if type == "Cat":
      newcat= Cat(name,age,breed, gender, vaccinated, image)
      newcat.add_new_cat()
   else:
      newdog= Dog(name,age,breed, gender, vaccinated, image)
      newdog.add_new_dog() 


# website routes

@app.route("/")
def home_page ():
   return render_template("index.html")

@app.route("/welcome")
def welcome_page():
   return render_template("welcome.html")

#sign in 
@app.route("/form_login", methods = ["POST", "GET"])
def login ():
  username = request.form["user_name"]
  p_w = request.form["password"]
  with open ("users_pw.json", "r") as f: 
     data = json.load(f)
     us = data["users"]
  for user in us: 
     if username == user["user_name"] and p_w == user["pass_word"]:      
         return render_template("welcome.html", name=username)  
            
     else:
         return render_template("index.html", info="invalid password")
  return render_template("index.html", info="invalid user")

# sign up page
@app.route("/sign-up", methods = ["POST", "GET"])
def sign ():
   username = request.form["user_name"]
   p_w = request.form["password"]
   p_w2 = request.form["password-two"]
   if p_w == p_w2:
      with open ("users_pw.json", "r") as f:
         data = json.load(f)
         us = data["users"] 
         temp = {
            "user_name": username, "pass_word": p_w
         }
         us.append(temp)
         with open ("users_pw.json", "w") as s:
            json.dump(data, s, indent=4)
         return render_template("index.html")
   else:
      return render_template("sign-up.html", info="your password does not match")

# takes the user inputs from the form
@app.route("/select-animal", methods = ["POST", "GET"])
def pet_for_adoption ():
   if request.method == "POST":
      results = request.form
      pet_type = request.form.get("adopt-animal")
      pet_name = request.form.get("name")
      pet_age = request.form.get("age")
      pet_breed = request.form.get("breed")
      pet_vaccinated= request.form.get("vaccinated")
      pet_gender = request.form.get("gender")
      pet_image = request.form.get("image")
      new_animal(pet_type, pet_name, pet_age, pet_breed, pet_vaccinated, pet_gender, pet_image)
      if pet_type == "Cat":
         return redirect('/cats')
      else:
         return redirect("/dogs")   


@app.route("/cats")
def cats_page ():
   with open("Cat.json") as json_file:
     data=json.load(json_file)
     cat_date=data["cats"]
   return render_template("cats.html", cats_data = cat_date)

@app.route("/dogs")
def dogss_page ():
   with open("Dog.json") as json_file:
      data = json.load(json_file)
      dog_data = data["dogs"]
   return render_template("dogs.html", dog_data = dog_data)

@app.route("/adoption")
def adoption_page ():
   return render_template("adoption.html")
      
@app.route("/shelter")
def shelter_page ():
   return render_template("shelter.html")

@app.route("/signup")
def sign_up ():
   return render_template("sign-up.html")

@app.route("/shop")
def shop ():
   with open("products.json") as json_file:
      data = json.load(json_file)
      product_data = data["products"]
   return render_template("shop.html", product_data = product_data)

# searching cats
@app.route("/search", methods = ["POST", "GET"])
def search_cat ():
   if request.method == "POST":
       cat_query = request.form.get("cat")
       result = ""
       with open("Cat.json") as s:
           data = json.load(s)
           arr = []
       for cat_data in data["cats"]:
         if cat_query in cat_data.values():
              arr.append(cat_data)
         else:
            result = "<p> no cats were found </p>"   
       return render_template("cats.html", cats_data = arr)
   

# searching dogs
@app.route("/search-dogs", methods = ["POST", "GET"])
def search_dogs ():
   if request.method == "POST":
       dog_query = request.form.get("dog")
       result = ""
       with open("Dog.json") as s:
           data = json.load(s)
           arr = []
       for dog_data in data["dogs"]:
         if dog_query in dog_data.values():
              arr.append(dog_data)
         else:
            result = "<p> no dogs were found </p>"   
       return render_template("dogs.html", dog_data = arr)
   
# implementing the adopted "delete" button    
@app.route("/delete/<name>", methods=["GET"])
def delete(name):
   with open('Cat.json', 'r') as f:
        data = json.load(f)
        data["cats"] = [cat for cat in data["cats"] if cat['name'] != name]
   with open('Cat.json', 'w') as f:
        json.dump(data, f, indent=4)
        return redirect("/cats")

# implementing the adopted "delete" button    
@app.route("/deletedog/<name>", methods=["GET"])
def deletedog(name):
   with open('Dog.json', 'r') as f:
        data = json.load(f)
        data["dogs"] = [dog for dog in data["dogs"] if dog['name'] != name]
   with open('Dog.json', 'w') as f:
        json.dump(data, f, indent=4)
        return redirect("/dogs")

if __name__ == "__main__":
   app.run(debug=True)