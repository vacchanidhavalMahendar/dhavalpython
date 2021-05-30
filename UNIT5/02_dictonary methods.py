myDict = {
    "dhaval":"in a fast manner",
    "dhavalmahendar":"spends a  lot of times in coding",
    "marks":[1,3,5],
     1:2232
} 
 #keys() methods
print(myDict.keys())       #prints the keys of the  dictionary

#values() methods
print(myDict.values())  #prints the values of the dictionary

#myDict.items()
print(myDict.items())

#myDict.update()
updateDict = {"psk":"dhaval"}
myDict.update(updateDict)
print(myDict)

#myDict.get()
print(myDict.get("dhaval"))