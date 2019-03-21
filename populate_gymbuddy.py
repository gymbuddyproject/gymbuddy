import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'wad2_group_project.settings')

import django
django.setup()
from gymbuddy.models import Gym, ProgressPics, Profile, Comments
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

def populate():
    #GYMS

    pure_gym_charing_cross = {
        "GymName" : "Pure Gym: Charing Cross",
        "Address" : "113 St George's Rd, Glasgow G3 6JA",
        "X_Coord" : 55.868682,
        "Y_Coord" : -4.270859,
        "Rating" :  4.5,
        "OpeningHours" : "Open 24 hours",
        "WebsiteURL" : "https://www.puregym.com/gyms/glasgow-charing-cross/",
    }

    xercise4less_glasgow= {
        "GymName": "Xercise4Less Glasgow Gym",
        "Address": "200 Sauchiehall St, Glasgow G2 3DZ",
        "X_Coord": 55.865486,
        "Y_Coord": -4.259427,
        "Rating": 3.5,
        "OpeningHours": "Monday - Friday: 6am-10pm, "
                        "Saturday - Sunday: 8am-8pm",
        "WebsiteURL":"https://www.xercise4less.co.uk/find-a-gym/glasgow-gym/" ,
    }

    nuffield_health_fitness = {
        "GymName": "Nuffield Health Fitness & Wellbeing Gym",
        "Address": "141 Finnieston St, Glasgow G3 8HB",
        "X_Coord":  55.859291,
        "Y_Coord":  -4.280722,
        "Rating": 3,
        "OpeningHours": "Monday - Friday: 6:30am-10pm, " \
                        "Saturday - Sunday: 8am-8pm",
        "WebsiteURL": "https://www.nuffieldhealth.com/gyms/glasgow-west-end",
    }

    pure_gym_hope_street = {
        "GymName" : "Pure Gym: Hope Street",
        "Address" : "67 Hope St, Glasgow G2 6AE",
        "X_Coord" : 55.860015,
        "Y_Coord" : -4.259349,
        "Rating" :  4.4,
        "OpeningHours" : "Open 24 hours",
        "WebsiteURL": "https://www.puregym.com/gyms/glasgow-hope-street/" ,
    }

    snap_fitness_glasgow = {
        "GymName" : "Snap Fitness Glasgow",
        "Address" : "95 Hope St, Glasgow G2 6LD",
        "X_Coord" : 55.860794,
        "Y_Coord" : -4.259423,
        "Rating" :  4.7,
        "OpeningHours" : "Open 24 hours",
        "WebsiteURL":"https://www.snapfitness.com/uk/gyms/glasgow-central/" ,
    }

    gyms = [pure_gym_charing_cross, xercise4less_glasgow,
            nuffield_health_fitness, pure_gym_hope_street,
            snap_fitness_glasgow]

    #PROFILES

    spic99 = {
        "username": "spic99",
        "email": "2324936c@student.gla.ac.uk",
        "password": "Glasgow617",
        "AboutMe": "I'm 20 years old and just moved to Glasgow for university. I'm relatively new to the world of fitness and would like to find an affordable nearby gym with good user ratings. I'd also like to find a more experienced partner to help show me the ropes.",
        "Following": [],
        "ProfilePicture": "spic99/profile_pic.jpg",
        "GymID": 1,
        "Height": 118,
        "Weight": 72,
        "Dob": "1999-02-18",
        "Experience": "Beginner",
    }

    K3LLy = {
        "username": "K3LLy",
        "email": "kellys1@gmail.com",
        "password": "K311y1",
        "AboutMe": "I'm 40 years old living in the West End of Glasgow. Veteran Powerlifter with a keen eye for strength. Looking for an equally determined training partner who can spot me and take pictures of my lifting. Hit me up if interested.",
        "Following": [spic99],
        "ProfilePicture": "K3LLy/profile_pic.jpg",
        "GymID": 2,
        "Height": 100,
        "Weight": 85,
        "Dob": "1979-02-21",
        "Experience": "Advanced",
    }

    ab96 = {
        "username": "ab96",
        "email": "annab87@outlook.com",
        "password": "Celtic67",
        "AboutMe": "22. Glasgow. Puregym. Usually in gym between 6 and 7 most evenings. Hmu if you want to go together.",
        "Following": [K3LLy, spic99],
        "ProfilePicture": "ab96/profile_pic.jpg",
        "GymID": 3,
        "Height": 162,
        "Weight": 55,
        "Dob": "1996-08-09",
        "Experience": "Intermediate"
    }

    aidan67 = {
        "username": "aidan67",
        "email": "aidsboy67@outlook.com",
        "password": "Lisbon67",
        "AboutMe": "Keen rugby player and enjoy heavy lifting in spair time. Let me know what you think of my progress pics. open to any tips you may have.",
        "Following": [K3LLy, ab96],
        "ProfilePicture": "aidan67/profile_pic.jpg",
        "GymID": 3,
        "Height": 200,
        "Weight": 115,
        "Dob": "1997-10-03",
        "Experience": "Intermediate"
    }

    frankub07 = {
        "username": "frankub07",
        "email": "frankrfc@outlook.com",
        "password": "St3veG123",
        "AboutMe": "Frank, Glasgow, 32. Member of Snap Fitness, due to work usually only in at weekends during the day. Always open to meeting new people and a gym buddy. I like to keep fit but don't lift too heavy weights so might not suit everyone. Let us know if you are interested.",
        "Following": [aidan67, K3LLy],
        "ProfilePicture": "frankub07/profile_pic.jpg",
        "GymID": 4,
        "Height": 183,
        "Weight": "78",
        "Dob": "1986-01-02",
        "Experience": "Intermediate"
    }
    profiles = [spic99, K3LLy, ab96, aidan67, frankub07]


    #PROGRESS PICS
#
    pp0 = {
        "UserName" : aidan67,
        "Photo" : "aidan67/progress_pics/1.jpg",
        "Likes" : 23,
    }
    pp1 = {
        "UserName": frankub07,
        "Photo": "frankub07/progress_pics/1.jpg",
        "Likes": 45,
    }

    pp2 = {
        "UserName": frankub07,
        "Photo": "frankub07/progress_pics/2.jpg",
        "Likes": 12,
    }

    pp3 = {
        "UserName": ab96,
        "Photo": "ab96/progress_pics/1.jpg",
        "Likes": 0,
    }

    pp4 = {
        "UserName": ab96,
        "Photo": "ab96/progress_pics/2.jpg",
        "Likes": 1,
    }

    pp5 = {
        "UserName": ab96,
        "Photo": "ab96/progress_pics/3.jpg",
        "Likes": 2,
    }
    pp6 = {
        "UserName": ab96,
        "Photo": "ab96/progress_pics/4.jpg",
        "Likes": 1,
    }

    pp7 = {
        "UserName": spic99,
        "Photo": "spic99/progress_pics/1.jpg",
        "Likes": 345,
    }

    pp8 = {
        "UserName": spic99,
        "Photo": "spic99/progress_pics/2.jpg",
        "Likes": 512,
    }
    pp9 = {
        "UserName": spic99,
        "Photo": "spic99/progress_pics/3.jpg",
        "Likes": 489,
    }
    pp10 = {
        "UserName": spic99,
        "Photo": "spic99/progress_pics/4.jpg",
        "Likes": 777,
    }

    progress_pics = [pp0,pp1,pp2,pp3,pp4,
                     pp5,pp6,pp7,pp8,pp9,
                     pp10]



    c0 = {
         "Poster" : spic99,
         "OnPic" : 3,
         "Date" : "2019-03-15 12:01",
         "Comment" : "Very good progress this week! Can't wait for the future!",
    }

    c1 = {
         "Poster": spic99,
         "OnPic": 1,
         "Date": "2019-03-15 12:15",
         "Comment" : "Very good my friend",
    }

    c2 = {
         "Poster": ab96,
         "OnPic": 4,
         "Date": "2019-03-15 08:09",
         "Comment": "Looks unreal hun x",
    }

    c3 = {
         "Poster": ab96,
         "OnPic":1,
         "Date": "2019-03-15 08:30",
         "Comment": "Nice work!",
    }

    c4 = {
         "Poster": K3LLy,
         "OnPic":9,
         "Date": "2019-03-15 14:09",
         "Comment": "Good work",
    }

    c5 = {
         "Poster": aidan67,
         "OnPic": 3,
         "Date": "2019-03-16 15:00",
         "Comment": "See you have been slacking this week, lol!!",
    }

    c6 = {
         "Poster" : frankub07,
         "OnPic": 2,
         "Date": "2019-03-16 15:07",
         "Comment": "Nice!",
    }

    c7 = {
         "Poster":frankub07,
         "OnPic": 6,
         "Date": "2019-03-16 15:21",
         "Comment":"5 stars, lol!",
    }

    c8 = {
         "Poster": frankub07,
         "OnPic":10,
         "Date": "2019-03-12 15:30",
         "Comment":"Yeah, okay I guess :/ ",
    }

    c9 = {
         "Poster": ab96,
         "OnPic": 3,
         "Date": "2019-03-12 16:00",
         "Comment": "Class!",
    }

    c10 = {
         "Poster":spic99,
         "OnPic": 4,
         "Date": "2019-03-17 21:00",
         "Comment": "Gj mate",
    }

    c11 = {
         "Poster": spic99,
         "OnPic": 8,
         "Date": "2019-03-17 21:05",
         "Comment":"Another great week!",
    }

    c12 = {
         "Poster": K3LLy,
         "OnPic": 9,
         "Date": "2019-03-17 21:55",
         "Comment":"Class!",
    }

    comments = [c0, c1, c2, c3, c4, c5, c6,
                c7, c8, c9, c10, c11, c12]

    for gym in gyms:
         gym_added = add_gym(gym["GymName"], gym["Address"], gym["X_Coord"], gym["Y_Coord"], gym["Rating"],
                             gym["OpeningHours"], gym["WebsiteURL"])

    for profile in profiles:
         following = []
         follow_grab = profile.get("Following", [])
         for followee in follow_grab:
              following.append(followee["username"])
         profile_added = add_profile(profile["username"], profile["email"], profile["password"], profile["AboutMe"], following,
                                  profile["ProfilePicture"], profile["GymID"], profile["Height"],
                                  profile["Weight"], profile["Dob"], profile["Experience"])

    for pic in progress_pics:
         pic_added = add_pic(pic["UserName"]["username"], pic["Photo"], pic["Likes"])

    for comment in comments:
         comment_added = add_comment(comment["Poster"]["username"], comment["OnPic"], comment["Date"], comment["Comment"])


def add_gym(GymName, Address, X_Coord, Y_Coord, Rating, OpeningHours, WebsiteURL):
    gym=Gym.objects.get_or_create(GymName=GymName, Address=Address, X_Coord=X_Coord,
                                  Y_Coord=Y_Coord, Rating=Rating, OpeningHours=OpeningHours,
                                  WebsiteURL=WebsiteURL)[0]
    gym.save()
    return gym

def add_user(username, email, password):
    password=make_password(password, hasher='pbkdf2_sha256')
    user = User.objects.get_or_create(username=username, email=email, password=password)[0]
    user.save()
    return user

def add_profile(username, email, password, AboutMe, Following, ProfilePicture, GymID, Height, Weight, Dob, Experience ):
    user = add_user(username, email, password)

    profile= Profile.objects.get_or_create(user=user,
                                           AboutMe=AboutMe, Following=Following, ProfilePicture=ProfilePicture, GymID=Gym.objects.get(id=GymID),
                                             Height=Height, Weight=Weight, DoB=Dob, Experience=Experience)[0]
    profile.save()
    return profile

def add_pic(UserName, Photo, Likes):
    user=User.objects.get(username=UserName)
    profile=Profile.objects.get(id=user.id)
    pic=ProgressPics.objects.get_or_create(UserName=profile, Photo=Photo, Likes=Likes)[0]
    pic.save()
    return pic

def add_comment(Poster, OnPic, Date, Comment):
    user = User.objects.get(username=Poster)
    profile = Profile.objects.get(id=user.id)
    onpic = ProgressPics.objects.get(PhotoID=OnPic)
    comment=Comments.objects.get_or_create(Poster=profile, OnPic=onpic, Date=Date, Comment=Comment)[0]
    comment.save()
    return comment


#Check correct
if __name__ == '__main__' :
    print("Starting population script")
    populate()



