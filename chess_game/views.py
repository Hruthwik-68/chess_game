from django.shortcuts import render, redirect
from .models import ChessGame

def index(request):
    game, created = ChessGame.objects.get_or_create(id=1)
    return render(request, 'chess_game/index.html', {'game': game, 'move': None})

def move_white(request):
    try:
        game = ChessGame.objects.get(id=1)
    except ChessGame.DoesNotExist:
        return redirect('index')

    move = game.move_white()
    return render(request, 'chess_game/index.html', {'game': game, 'move': move})

def move_black(request):
    try:
        game = ChessGame.objects.get(id=1)
    except ChessGame.DoesNotExist:
        return redirect('index')

    move = game.move_black()
    return render(request, 'chess_game/index.html', {'game': game, 'move': move})
def restart_game(request):
    game = ChessGame.objects.first()  
    game.restart_game()
    return redirect('index')  
