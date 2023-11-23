# write your code here
def regexp(regex, string, regex_default=[]):
    if not regex_default:
        regex_default = regex
        
    if not regex:
        return True
    if not string:
        return True if regex[0] == '$' else False
    if regex[0] == '^':
        if regex[1] in ['.', string[0]]:
            return regexp(regex[1:], string)
        return False
    
    # Condition not working properly with metadata after \
    # Like \.+|end. but works with \.$|end.
    if regex[0] == "\\":
        if regex[1] == string[0]:
            return regexp(regex[2:], string[1:], regex_default)
        return regexp(regex, string[1:])
        
    if len(regex) > 1:
        if regex[1] in '?*+':
            if regex[0] in ['.', string[0]]:
                if len(string) == 1:
                    return True
                if regex[1] == '?':
                    return regexp(regex[2:], string[1:], regex_default)
                if regex[1] == '+':
                    if string[0] != string[1]:
                        return regexp(regex[2:], string[1:], regex_default)
                return regexp(regex, string[1:], regex_default)
            if regex[1] in '?*':
                return regexp(regex[2:], string, regex_default)
            return False
            
    if regex[0] in ['.', string[0]]:
        return regexp(regex[1:], string[1:], regex_default)
        
    regex = regex_default
    return regexp(regex, string[1:])

print(regexp(*input().split('|')))
