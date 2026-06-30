class Config:
    theme = "light"
    
try:
    mode = input()
    obj = Config()
    
    if mode == "CLASS":
        Config.theme = "dark"
    elif mode == "INSTANCE":
        obj.theme = "dark"
    else:
        raise ValueError
        
    print(f"CLASS={Config.theme} OBJ={obj.theme}")
except:
    print("BAD")