

def formatViews(views_text):
    views_text = views_text.replace(",", "")
    views_text = views_text.replace(" views", "")
    return int(float(views_text))

def formatDuration(duration):
    duration = duration.replace("- Duration: ", "")
    l = duration.split(':')
    sec = 0
    c = len(l)
    for i in range(c):
        sec += int(float(l[i]))*pow(60, c - i - 1)
    return sec