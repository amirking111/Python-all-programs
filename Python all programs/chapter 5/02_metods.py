myDict ={
    "fast" : "in a quick manner",
    "harry": "a coder",
    "marks" : [1,2,3],
    "anotherDict": {"harry" : "player"},
    1 : 2
}

#dictionart methods
print(list(myDict.keys())) # printe the keys of the dictinary
print(myDict.values()) # prints the keys of the dictionary
print(myDict.items()) # prints the keys , value for all contents of the dictionary
print(myDict)
updateDict ={
    "love" : "friend",
    "shubham" : "friends",
    "harry": "a dancer"


}
myDict.update(updateDict) #update the dictionary by addimg key value pairs from updatedDict

print(myDict)

print(myDict.get("harry"))