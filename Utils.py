

def formatViews(views_text):
    views_text = views_text.replace(",", "")
    views_text = views_text.replace(" views", "")
    return int(float(views_text))

def formatDuration(duration):
    # TODO: get duration in sec (with regex?)
    return duration