import os


def __extract_args (args) : 
    new_args = []
    for i in args : 
        if type(i) == str:
                new_args.append(i[1:-1])
        elif type(i) == tuple : 
            var_type = i[0]
            var_value = i[1]
            if var_value == str:
                var_value = var_value.strip()
                if var_type == str :
                    if var_value.startswith('"') and var_value.endswith('"') :
                        var_value = var_value[1:-1]
                
            new_args.append(var_type(var_value))
    return new_args
    
def cleanScreen (*args) :
    os.system('cls')

def write (*args) :
    for i in __extract_args(args): 
        print(i)

def userInput(*args): 
    var_manager = args[-1]
    var_type = args[0][0]
    var_key = args[0][2]
    var_value = args[-2]
    if var_type == bool : 
        val = var_type(int(input(var_value[1:-1])))
    else:    
        val = var_type(input(var_value[1:-1]))
    var_manager.set_var(
        var_manager.get_rtype(var_type),
        var_key,
        val
    )
    return var_manager