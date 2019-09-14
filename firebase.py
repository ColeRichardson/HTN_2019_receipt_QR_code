import pyrebase

config = {
    "apiKey": "AIzaSyCPRMbgyE6_mR9PK451sIEUQ3Jp4-bc24Y",
    "storageBucket": "httn-e697c.appspot.com",
    "databaseURL": "httn-e697c.firebaseio.com/",
    "authDomain": "httn-e697c.firebaseio.com"
}

def get_rand_string():
    import uuid
    return uuid.uuid4().hex    

def upload_and_return_url(file_path):
    firebase = pyrebase.initialize_app(config)
    storage = firebase.storage()
    filename_on_firebase = get_rand_string()
    storage.child(filename_on_firebase).put(file_path)
    return storage.child(filename_on_firebase).get_url("")

if __name__ == "__main__":
    firebase = pyrebase.initialize_app(config)
    storage = firebase.storage()
    #storage.child("README_firebase.md").put("README.md")

    print(storage.child("README_firebase.md").get_url(""))
    
    output_filename = get_rand_string()
    storage.child("README_firebase.md").download(output_filename)



