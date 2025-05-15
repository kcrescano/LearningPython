# mine
def heading(text, level=1):
    level = 1 if level < 1 else 6 if level > 6 else level
    return f'{level * "#"} {text}'
# Hpyerskill user posted solution
def heading(text, level=1):
    return '#' * min(max(1, level), 6) + ' ' + text
