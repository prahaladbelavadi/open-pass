import json

client = raw_input("Enter client name:")
url = raw_input("Enter web URL:")
meta = raw_input("Enter any meta data:")

data = {
'name': client,
'url':url,
'meta':meta
}

print data

with open('data.json', 'w') as f:
     json.dump(data, f)

file_state = open("filename.txt", "a")
file_state.write('\n'+client+'\n')
file_state.write('\n'+url+'\n')
file_state.write('\n'+meta+'\n')

file_state.close
