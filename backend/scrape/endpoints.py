def sodexo_login_url(username: str, password: str) -> str:
    # note: we dont actaully need the __ncforminfo tag to login
    return f"https://bing.campuscardcenter.com/ch/login.html?username={username}&password={password}&action=Login"

def account_url(id: str): 
    return f"https://bing.campuscardcenter.com/ch/accountList.html?id={id}"

