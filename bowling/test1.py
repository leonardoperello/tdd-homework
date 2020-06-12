from funciones import play_bowling

def test_all_gutter():
    result = play_bowling(current_score = 0,  rolls = 20, pins = 0)
    assert result == 0

def test_all_ones():
    result = play_bowling(current_score = 0, rolls = 20, pins = 1)
    assert result == 20

def test_spare():
        result = play_bowling(current_score = 0, rolls = 1, pins = 2)
        # cuando se tiran todos los pinos en 2 intento, se suma
        # al score **proximoTiro**
        # la cantidad de pinos tirados en la
        # 1er oportunidad del tiro extra
        result = play_bowling(current_score = result, rolls = 1, pins = 8)
        proximoTiro = 1
        result = play_bowling(current_score = result+proximoTiro, rolls = 18, pins = proximoTiro)
        assert result == 29

def test_strike():
    # cuando hago un strike me suma al 1er turno lo que tiro en el siguiente
    # y en el 2do turno me da como resultado lo del primero mas lo que tire en el 2do
    result = play_bowling(current_score = 0, rolls = 1, pins = 10)
    result = play_bowling(current_score = result, rolls = 2, pins = 2)
    assert result == 14