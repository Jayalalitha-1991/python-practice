from django.shortcuts import render
from .coin_flip import CoinFlipGame

def coin_flip_view(request):
    result = None
    user_choice = None
    coin_flip = None

    if request.method == 'POST':
        user_choice = request.POST.get('choice')
        game = CoinFlipGame()
        game.get_user_choice(user_choice)
        game.flip_coin()
        result = game.get_result()
        coin_flip = game.coin_flip

    return render(request, 'game/coin_flip.html', {
        'result': result,
        'user_choice': user_choice,
        'coin_flip': coin_flip
    })
