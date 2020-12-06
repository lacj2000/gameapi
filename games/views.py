from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from games.models import Game
from games.serializers import GameSerializer
from datetime import datetime
import pytz


@api_view(['GET','POST'])
def game_list(request):
    if request.method == 'GET':
        games = Game.objects.all()
        games_serializer = GameSerializer(games, many=True)
        return Response(games_serializer.data)
    elif request.method == 'POST': 
        game_serializer = GameSerializer(data=request.data)
        if game_serializer.is_valid():
            try:
                games = Game.objects.get(name=request.data['name'])
                if bool(games):
                    return Response({"name":"game already exists in the database"}, status=status.HTTP_400_BAD_REQUEST)
            except:
                game_serializer.save()
                return Response(game_serializer.data, status=status.HTTP_201_CREATED) 
        return Response(game_serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET','PUT','DELETE'])
def game_detail(request, pk):
    try:
        game = Game.objects.get(id=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        game_serializer = GameSerializer(game)
        return Response(game_serializer.data, status=status.HTTP_200_OK)  
    elif request.method == "PUT":
        game_serializer = GameSerializer(game, data=request.data)
        if game_serializer.is_valid():
            try:
                games = Game.objects.filter(name=request.data['name'])         
                if not game in games:
                    return Response({"name":"game already exists in the database"}, status=status.HTTP_400_BAD_REQUEST)
                else:
                    game_serializer.save()
                    return Response(game_serializer.data)
            except:
                game_serializer.save()
                return Response(game_serializer.data)
        return Response(game_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        utc=pytz.UTC
        date2 = utc.localize(datetime.now())
        print(date2)
        # date1 = utc.localize(game.release_date)
        # print(date1)
        if game.release_date > date2:        
            game.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({"date_release":"Game has been released"},status=status.HTTP_401_UNAUTHORIZED)