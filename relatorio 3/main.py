from database import Database
from helper.WriteAJson import writeAJson

db = Database(database="pokedex", collection="pokemons")
db.resetDatabase()

pokemons_dataset = db.collection.find()

git remote add origin https://github.com/warleyruivo/s202-lab.git
git branch -M main
git push -u origin main