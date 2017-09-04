
# Format two dates based on months and years - assumes start date is before end date
def format_date_month_year(start_date, end_date):

    # If month and years are same
    if start_date.month == end_date.month and start_date.year == end_date.year:
        return start_date.strftime("%B %Y")

    # If years are same but months are not
    elif start_date.year == end_date.year:
        start_date = start_date.strftime("%B")
        end_date = end_date.strftime("%B %Y")

    # If months are different
    else:
        start_date = start_date.strftime("%B %Y")
        end_date = end_date.strftime("%B %Y")

    return start_date + " - " + end_date


# Format two dates based on month and day
def format_date_month_day(start_date, end_date):

    # If month and day are the same
    if start_date.month == end_date.month and start_date.day == end_date.day:
        return start_date.strftime("%B %d").lstrip("0").replace(" 0", " ")

    # If month is the same
    elif start_date.month == end_date.month:
        start_date = start_date.strftime("%B %d").lstrip("0").replace(" 0", " ")
        end_date = end_date.strftime("%d").lstrip("0").replace(" 0", " ")

    # If months are different
    else:
        start_date = start_date.strftime("%B %d").lstrip("0").replace(" 0", " ")
        end_date = end_date.strftime("%B %d").lstrip("0").replace(" 0", " ")

    return start_date + " - " + end_date
