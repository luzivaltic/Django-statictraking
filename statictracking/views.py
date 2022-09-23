from time import time
from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
from django.urls import reverse 
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.models import User
from .models import Game , Username , Property

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect( reverse("login") )
    username = Username.objects.filter( username = request.user.username ).first()
    if username == None:
        return HttpResponseRedirect( reverse("logout") )

    games = Game.objects.filter( game_user = username ).all()
    game_played = games.count()
    win_rate = games.filter( game_res = True ).all().count()

    if game_played == 0:
        win_rate = 0
    else:
        win_rate = int( win_rate / game_played  * 100 )
    cs = []
    death = []
    time = []
    for game in games:
        cs.append( game.cs )
        death.append( game.death )
        time.append( game.time )
    
    properties = username.user_property.all()
    property = []

    for content in properties:
        if content.property_content == "":
            username.user_property.remove(content)
        total_games = content.games.filter( game_user = username ).all().count()
        win_games = content.games.filter( game_user = username ).filter( game_res = True ).all().count()
        if total_games != 0 :
            property.append ([ total_games,int(win_games / total_games * 100 )])
        else :
            property.append( [ 0 , 0 ] )

    return render(request , "statictracking/index.html" , {
        "games" : games,
        "game_played" : game_played,
        "win_rate" : win_rate,
        "cs" : cs,
        "death" : death,
        "time" : time,
        "property" : property,
        "properties": properties,
    })

def login_views(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request , username=username , password = password)
        if user is not None:
            login(request , user)
            return HttpResponseRedirect( reverse("index") )
        else:
            return render( request , "statictracking/login.html",  {
                "message" : "Invalid login."   
            })

    return render( request , "statictracking/login.html" )

def logout_views(request):
    logout(request)
    return render(request , "statictracking/login.html", {
        "message" : "Logged out",
    })

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate( request , username = username , password = password )
        if user is None: 
            user = User.objects.create_user(username = username , password = password)
            new_user = Username.objects.create( username = username )
        return HttpResponseRedirect( reverse("login") )

    return render(request , "statictracking/register.html")

def add_property(request):
    if request.method == "POST":
        username = Username.objects.filter( username = request.user.username ).first()
        if request.POST["new_property"] == "":
            return HttpResponseRedirect( reverse("index") )
        new_property = Property.objects.filter( property_content = request.POST["new_property"] ).first()
        if new_property == None:
            new_property = Property.objects.create( property_content = request.POST["new_property"] )
        new_property.user.add( username )
    
    return HttpResponseRedirect( reverse("index") )

def delete_property(request , content ):  
    username = Username.objects.get( username = request.user.username )
    cur_property = Property.objects.get( property_content = content )
    cur_property.user.remove(username)
    all_related_game = Game.objects.filter( game_user = username ).all()
    for cur_game in all_related_game:
        cur_game.game_properties.remove( cur_property )
    return HttpResponseRedirect( reverse("index") )

def add_game(request):
    if request.method == "POST":
        win_game = request.POST.get("game-result", False)
        if win_game != False:
            win_game = True
        
        cur_user = Username.objects.get( username = request.user.username )
        new_game = Game.objects.create(
            game_user = cur_user,
            game_res = win_game,
            cs = request.POST["cs"],
            death = request.POST["death"],
            time = request.POST["time"],
        )

        cur_property = cur_user.user_property.all()
        for property in cur_property:
            box_check = request.POST.get(property.property_content , False)
            if box_check != False:
                new_game.game_properties.add( property )

    return HttpResponseRedirect( reverse("index") )

def delete_game(request):
    Game.objects.last().delete()
    return HttpResponseRedirect( reverse("index") )