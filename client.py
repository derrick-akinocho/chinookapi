#client.py
import requests
import argparse
import json

# Menu display
print("\n--------------------------------WELCOME-TO-CHINOOK--------------------------------\n")
print("Please select : \n (1) to display artists with the same name, \n (2) to display album names corresponding to an artist, \n (3) to display track names corresponding to an album \n")

"""
 Get a valid integer from the user.
 This function expects an integer,then returns this integer if the conversion is successful. 
"""
def getValidInteger(message):

    while True:
        try:
            x = int(input(f"{message} \n "))
            return x  # If conversion to integer is successful, return the value

        except ValueError:
            print("Please enter a valid integer.\n")

"""
 This function expects an option between 1, 2, 3 and displays the result
"""
def getArgs(valeur):

    if valeur == 1 :

        x = input("An artist's name : ")
        args = {"artistName" : x}

        return (f"\n Here are the artists with the same name as {x} \n" + switch_case(args) + "\n")

    elif valeur == 2 :

        x = getValidInteger("An artist's identifier : ")
        args = {"artistId" : x}

        return (f"\n Here are the album names corresponding to the artist identified by {x} \n" + switch_case(args) + "\n")

    elif valeur == 3 :

        x = getValidInteger("An album's identifier : ")
        args = {"albumId" : x}

        return (f"\n  Here are the track names corresponding to album identified by {x} \n" + switch_case(args) + "\n")

    else :
        return "No orders are allocated to " + valeur

"""
This function expects an attribute, which can be an integer or a character string. 
It then executes get requests and returns the result.
"""
def switch_case(args):

    # URL of HTTP request to web API.
    url = "http://127.0.0.1:8000/"

    if "artistId" in args and args["artistId"] != "" :
        # Makes a GET request to the specified URL and contains the HTTP request response
        query = requests.get(url + "albums/?artistId=" + str(args["artistId"]))

        # Loading JSON, json.dumps() formats JSON in a readable way
        data = json.loads(query.text)
        title = []

        for item in data:
            title.append(item['title'])

        formatted_json = json.dumps(title, indent=4, sort_keys=True)

        # Returns the query response
        return formatted_json

    elif "artistName" in args and args["artistName"] != "" :
        # Makes a GET request to the specified URL and contains the HTTP request response
        query = requests.get(url + "artists/?name=" + args["artistName"])

        # Loading JSON, json.dumps() formats JSON in a readable way
        data = json.loads(query.text)
        name = []

        # Returns the query response
        for item in data:
            name.append(item['name'])

        formatted_json = json.dumps(name, indent=4, sort_keys=True)
        
        # Returns the query response
        return (formatted_json)

    elif "albumId" in args and args["albumId"] != "" :
        # Makes a GET request to the specified URL and contains the HTTP request response
        query = requests.get(url + "tracks/?albumId=" + str(args["albumId"]))

        # Loading JSON, json.dumps() formats JSON in a readable way
        data = json.loads(query.text)
        name = []

        # Returns the query response
        for item in data:
            name.append(item['name'])

        formatted_json = json.dumps(name, indent=4, sort_keys=True)
        
        # Returns the query response
        return (formatted_json)

    else:
        # Returns a message if args does not match any expected value 
        return 'No data entered'

print("\n CHINOOK response : ", getArgs(getValidInteger("What to display ?")))