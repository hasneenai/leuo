from fake_useragent import UserAgent

def generate_user_agent():
    ua = UserAgent()
    return ua.random
