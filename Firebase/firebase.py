import pyrebase


firebaseConfig = {
    'apiKey': "AIzaSyAiSuhBQNTgBAnL8-j6KcVksPBSpt-c7Bc",
    'authDomain': "fir-96fc3.firebaseapp.com",
    'databaseURL' : "https://fir-96fc3.firebaseio.com",
    'projectId': "fir-96fc3",
    'storageBucket': "fir-96fc3.appspot.com",
    'messagingSenderId': "928851673689",
    'appId': "1:928851673689:web:285bc84c01dc4e4980e748",
    'measurementId': "G-3QG74644C3"
  }

firebase = pyrebase.initialize_app(firebaseConfig)

#db=firebase.database()
auth=firebase.auth()
storage=firebase.storage()


#Authentication--.Login

'''email=input('Enter your Email  ')
password=input('Enter your password  ')
try:
  auth.sign_in_with_email_and_password(email,password)
  print("Successfully signed in")

except:
  print("Invalid email or password")'''

# SignUp

'''email=input('Enter your Email  ')
password=input('Enter your password  ')
configpass=input('Confirm Password')
if password==configpass:
  auth.create_user_with_email_and_password(email,password)'''


#Storage
filename = input('Enter the of the file you want to upload')
cloudfilename = input('Enter name of file on cloud')
storage.child(cloudfilename).put(filename)
#print the url of the file
print(storage.child(cloudfilename).get_url(None))

#Download the file
'''cloudfilename=input('Enter the file name to download')
storage.child(cloudfilename).download("",'downloded.txt')'''






