#problema 13
def get_temp(x, val_i, val_f):
    if val_i == 'C' :
        if val_f == 'F' :
            x = x * 1.8 + 32
        if val_f == 'K' :
            x = x + 273.15
    if val_i == 'F' :
        if val_f == 'C' :
            x = (x - 32) * 5/9
        if val_f == 'K' :
            x = (x - 32) / 1.8 + 273.15
    if val_i == 'K' :
        if val_f == 'C' :
            x = x - 273.15
        if val_f == 'F' :
            x = (x - 273.15) * 1.8 + 32
    return x

def test_get_temp() :
    assert (get_temp(27, 'C', 'K') == 174.9) is False
    assert (get_temp(327.15, 'K', 'C') == 54) is True
    assert (get_temp(85, 'F', 'C') == 29.44) is True