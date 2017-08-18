
# Format two dates based on months and years - assumes start date is before end date
def format_two_dates(start_date, end_date):

    # If month and years are same
    if start_date.month == end_date.month and start_date.year == end_date.year:
        start_date = start_date.strftime("%B %Y")
        end_date = None
        return start_date

    # If years are same but months are not
    elif start_date.year == end_date.year:
        start_date = start_date.strftime("%B")
        end_date = end_date.strftime("%B %Y")

    # If months are different
    else:
        start_date = start_date.strftime("%B %Y")
        end_date = end_date.strftime("%B %Y")

    return start_date + " - " + end_date
