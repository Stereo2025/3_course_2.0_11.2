def str_func(string: str) -> str:
    """dockstring add other changes"""
    return string.upper()


def second_func(string: str) -> str:
    """"dockstring"""
    """Fix bag from this func"""
    try:
        return string.title()
    except BaseException as b:
        print(b)
    finally:
        print('ТарамПамПам')
