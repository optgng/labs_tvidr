
def calc_rgb_to_ycrcb(r: int, g: int, b: int):
    y = 0.299*r + 0.587*g + 0.114*b
    cr = 0.5*r - 0.419*g - 0.081*b
    cb = -0.169*r - 0.331*g + 0.5*b
    return round(y), round(cr), round(cb)  # y, cr, cb
