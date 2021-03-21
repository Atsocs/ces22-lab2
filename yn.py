def yes_or_no(prompt=""):
    r = input(prompt + ' Press Y-yes or N-no.').lower()
    if r in ['y', 'yes', 'yep']:
        return True
    elif r in ['n', 'no', 'not', 'nope']:
        return False
    else:
        print("Sorry, try again.")
        return yes_or_no(prompt)
