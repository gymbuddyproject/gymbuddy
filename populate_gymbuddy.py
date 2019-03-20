import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'wad2_group_project.settings')

import django
django.setup()
from gymbuddy.models import Gym, ProgressPics, Profile, Comments
from django.contrib.auth.models import User

def populate():
    #GYMS

    pure_gym_charing_cross = {
        "GymName" : "Pure Gym: Charing Cross",
        "Address" : "113 St George's Rd, Glasgow G3 6JA",
        "X_Coord" : 55.868682,
        "Y_Coord" : -4.270859,
        "Rating" :  4.5,
        "OpeningHours" : "Open 24 hours",
    }

    xercise4less_glasgow= {
        "GymName": "Xercise4Less Glasgow Gym",
        "Address": "200 Sauchiehall St, Glasgow G2 3DZ",
        "X_Coord": 55.865486,
        "Y_Coord": -4.259427,
        "Rating": 3.5,
        "OpeningHours": "Monday - Friday: 6am-10pm, "
                        "Saturday - Sunday: 8am-8pm",
    }

    nuffield_health_fitness = {
        "GymName": "Nuffield Health Fitness & Wellbeing Gym",
        "Address": "141 Finnieston St, Glasgow G3 8HB",
        "X_Coord":  55.859291,
        "Y_Coord":  -4.280722,
        "Rating": 3,
        "OpeningHours": "Monday - Friday: 6:30am-10pm, " \
                        "Saturday - Sunday: 8am-8pm",
    }

    pure_gym_hope_street = {
        "GymName" : "Pure Gym: Hope Street",
        "Address" : "67 Hope St, Glasgow G2 6AE",
        "X_Coord" : 55.860015,
        "Y_Coord" : -4.259349,
        "Rating" :  4.4,
        "OpeningHours" : "Open 24 hours",
    }

    snap_fitness_glasgow = {
        "GymName" : "Snap Fitness Glasgow",
        "Address" : "95 Hope St, Glasgow G2 6LD",
        "X_Coord" : 55.860794,
        "Y_Coord" : -4.259423,
        "Rating" :  4.7,
        "OpeningHours" : "Open 24 hours",
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
        "ProfilePicture": "/media/spic99/profile_pic.jpg",
        "GymID": 1,
        "Height": 118,
        "Weight": 72,
        "Dob": "18/02/1999",
        "Experience": "Beginner",
    }

    K3LLy = {
        "username": "K3LLy",
        "email": "kellys1@gmail.com",
        "password": "K311y1",
        "AboutMe": "I'm 40 years old living in the West End of Glasgow. Veteran Powerlifter with a keen eye for strength. Looking for an equally determined training partner who can spot me and take pictures of my lifting. Hit me up if interested.",
        "Following": [spic99],
        "ProfilePicture": "/media/K3LLy/profile_pic.jpg",
        "GymID": 2,
        "Height": 100,
        "Weight": 85,
        "Dob": "17/01/1979",
        "Experience": "Advanced",
    }

    ab96 = {
        "username": "ab96",
        "email": "annab87@outlook.com",
        "password": "Celtic67",
        "AboutMe": "22. Glasgow. Puregym. Usually in gym between 6 and 7 most evenings. Hmu if you want to go together.",
        "Following": [K3LLy, spic99],
        "ProfilePicture": "/media/ab96/profile_pic.jpg",
        "GymID": 3,
        "Height": 162,
        "Weight": 55,
        "Dob": "17/12/1996",
        "Experience": "Intermediate"
    }

    aidan67 = {
        "username": "aidan67",
        "email": "aidsboy67@outlook.com",
        "password": "Lisbon67",
        "AboutMe": "Keen rugby player and enjoy heavy lifting in spair time. Let me know what you think of my progress pics. open to any tips you may have.",
        "Following": [K3LLy, ab96],
        "ProfilePicture": "/media/aidan67/profile_pic.jpg",
        "GymID": 3,
        "Height": 200,
        "Weight": 115,
        "Dob": "02/10/1997",
        "Experience": "Intermediate"
    }

    frankub07 = {
        "username": "frankub07",
        "email": "frankrfc@outlook.com",
        "password": "St3veG123",
        "AboutMe": "Frank, Glasgow, 32. Member of Snap Fitness, due to work usually only in at weekends during the day. Always open to meeting new people and a gym buddy. I like to keep fit but don't lift too heavy weights so might not suit everyone. Let us know if you are interested.",
        "Following": [aidan67, K3LLy],
        "ProfilePicture": "/media/frankub07/profile_pic.jpg",
        "GymID": 4,
        "Height": 183,
        "Weight": "78",
        "Dob": "17/05/1986",
        "Experience": "Intermediate"
    }
    profiles = [spic99, K3LLy, ab96, aidan67, frankub07]


    #PROGRESS PICS
#
    pp0 = {
        "UserName" : aidan67,
        "Photo" : "/media/aidan67/progress_pics/1.jpg",
        "Likes" : 23,
    }
    pp1 = {
        "UserName": frankub07,
        "Photo": "/media/frankub07/progress_pics/1.jpg",
        "Likes": 45,
    }

    pp2 = {
        "UserName": frankub07,
        "Photo": "/media/frankub07/progress_pics/2.jpg",
        "Likes": 12,
    }

    pp3 = {
        "UserName": ab96,
        "Photo": "/media/ab96/progress_pics/1.jpg",
        "Likes": 0,
    }

    pp4 = {
        "UserName": ab96,
        "Photo": "/media/ab96/progress_pics/2.jpg",
        "Likes": 1,
    }

    pp5 = {
        "UserName": ab96,
        "Photo": "/media/ab96/progress_pics/3.jpg",
        "Likes": 2,
    }
    pp6 = {
        "UserName": ab96,
        "Photo": "/media/ab96/progress_pics/4.jpg",
        "Likes": 1,
    }

    pp7 = {
        "UserName": spic99,
        "Photo": "/media/spic99/progress_pics/1.jpg",
        "Likes": 345,
    }

    pp8 = {
        "UserName": spic99,
        "Photo": "/media/spic99/progress_pics/2.jpg",
        "Likes": 512,
    }
    pp9 = {
        "UserName": spic99,
        "Photo": "/media/spic99/progress_pics/3.jpg",
        "Likes": 489,
    }
    pp10 = {
        "UserName": spic99,
        "Photo": "/media/spic99/progress_pics/4.jpg",
        "Likes": 777,
    }

    progress_pics = [pp0,pp1,pp2,pp3,pp4,
                     pp5,pp6,pp7,pp8,pp9,
                     pp10]



    c0 = {
         "Poster" : spic99,
         "OnPic" : pp3,
         "Date " : "15/03/2019",
         "Comment" : "Very good progress this week! Can't wait for the future!",
    }

    c1 = {
         "Poster": spic99,
         "OnPic": pp1,
         "Date ": "15/03/2019",
         "Comment" : "Very good my friend",
    }

    c2 = {
         "Poster": ab96,
         "OnPic": pp4,
         "Date ": "15/03/2019",
         "Comment": "Looks unreal hun x",
    }

    c3 = {
         "Poster": ab96,
         "OnPic":pp1,
         "Date ": "15/03/2019",
         "Comment": "Nice work!",
    }

    c4 = {
         "Poster": K3LLy,
         "OnPic":pp9,
         "Date ": "15/03/2019",
         "Comment": "Good work",
    }

    c5 = {
         "Poster": aidan67,
         "OnPic": pp0,
         "Date ": "12/03/2019",
         "Comment": "See you have been slacking this week, lol!!",
    }

    c6 = {
         "Poster" : frankub07,
         "OnPic": pp2,
         "Date ": "12/03/2019",
         "Comment": "Nice!",
    }

    c7 = {
         "Poster":frankub07,
         "OnPic": pp6,
         "Date ": "12/03/2019",
         "Comment":"5 stars, lol!",
    }

    c8 = {
         "Poster": frankub07,
         "OnPic":pp10,
         "Date ": "12/03/2019",
         "Comment":"Yeah, okay I guess :/ ",
    }

    c9 = {
         "Poster": ab96,
         "OnPic": pp3,
         "Date ": "12/03/2019",
         "Comment": "Class!",
    }

    c10 = {
         "Poster":spic99,
         "OnPic": pp4,
         "Date ": "12/03/2019",
         "Comment": "Gj mate",
    }

    c11 = {
         "Poster": spic99,
         "OnPic": pp8,
         "Date ": "12/03/2019",
         "Comment":"Another great week!",
    }

    c12 = {
         "Poster": K3LLy,
         "OnPic": pp9,
         "Date ": "11/03/2019",
         "Comment":"Class!",
    }

    comments = [c0, c1, c2, c3, c4, c5, c6,
                c7, c8, c9, c10, c11, c12]

    for gym in gyms:
         gym_added = add_gym(gym["GymName"], gym["Address"], gym["X_Coord"], gym["Y_Coord"], gym["Rating"], gym["OpeningHours"])

    for profile in profiles:
         following = []
         follow_grab = profile.get("Following", [])
         for followee in follow_grab:
              following.append(followee["username"])
         print(following)
         profile_added = add_profile(profile["username"], profile["email"], profile["password"], profile["AboutMe"], following,
                                  profile["ProfilePicture"], profile["GymID"], profile["Height"],
                                  profile["Weight"], profile["Dob"], profile["Experience"])

    for pic in progress_pics:
         pic_added = add_pic(pic["UserName"]["username"], pic["Photo"], pic["Likes"])

    for comment in comments:
         comment_added = add_comment(comment["CommentID"], comment["Poster"], comment["OnPic"], comment["Date"], comment["Comment"])


def add_gym(GymName, Address, X_Coord, Y_Coord, Rating, OpeningHours):
    gym=Gym.objects.get_or_create(GymName=GymName, Address=Address, X_Coord=X_Coord, Y_Coord=Y_Coord, Rating=Rating, OpeningHours=OpeningHours)[0]
    gym.save()
    return gym

def add_user(username, email, password):
    user = User.objects.get_or_create(username=username, email=email, password=password)[0]
    user.save()
    return user

def add_profile(username, email, password, AboutMe, Following, ProfilePicture, GymID, Height, Weight, Dob, Experience ):
    user = add_user(username, email, password)

    profile= Profile.objects.get_or_create(user=user,
                                           AboutMe=AboutMe, Following=Following, ProfilePicture=ProfilePicture, GymID=Gym.objects.get(id=GymID),
                                             Height=Height, Weight=Weight, DoB='1999-12-12', Experience=Experience)[0]
    profile.save()
    return profile

def add_pic(UserName, Photo, Likes):

    pic=ProgressPics.objects.get_or_create(UserName=UserName, Photo=Photo, Likes=Likes)[0]
    pic.save()
    return pic

def add_comment(Poster, OnPic, Date, Comment):
    comment=Comment.objects.get_or_create(Poster=Poster, OnPic=OnPic, Date=Date, Comment=Comment)[0]
    comment.save()
    return comment


#Check correct
if __name__ == '__main__' :
    print("Starting population script")
    populate()



