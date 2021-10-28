def how_many_seconds(days, hours, minutes, seconds):
    
    if days < 0 or hours < 0 or minutes < 0 or seconds < 0:
        raise ValueError("Values cannot be negative!")

    return days*24*60*60 + hours*60*60 + minutes*60 + seconds