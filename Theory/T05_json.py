import json

# In detail in password generator program
new_data = {
        website: {
            "email":email,
            "password":password,
        }
    }


with open("data.json", "w") as data_file:
            json.dump(new_data,data_file,indent=4) # json.dump = file.write (dictionary name,file variable name,to indent and clear the output to user)

            # data = json.load(data_file)     # json.load = file.read(file name) and must open the file in read mode
            # print(data)

            # Reading old data
            data = json.load(data_file)
            # Updating old data with new data
            data.update(new_data)
            # Saving updated data
            json.dump(data,data_file,indent=4)