from django.shortcuts import render

import pyrebase

firebaseConfig = {
    'apiKey': "AIzaSyAPD0VQwd7xiOX8zGFD4A_mDMOELYlE6lU",
    'authDomain': "django-firebase-b2b5b.firebaseapp.com",
    'databaseURL' : "https://django-firebase-b2b5b.firebaseio.com",
    'projectId': "django-firebase-b2b5b",
    'storageBucket': "django-firebase-b2b5b.appspot.com",
    'messagingSenderId': "230449047748",
    'appId': "1:230449047748:web:de5231adbd756b266d4191",
    'measurementId': "G-LPS2DDDQMV"
  }

firebase = pyrebase.initialize_app(firebaseConfig)

#db=firebase.database()
auth=firebase.auth()

def signIn(request):
    return render(request, "signIn.html")

def postsign(request):
    email=request.POST.get('email')
    passw=request.POST.get('pass')

    user=auth.sign_in_with_email_and_password(email,passw)
    return render(request, "welcome.html", {"e":email})