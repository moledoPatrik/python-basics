month_conversions = {
    'Jan': 'January',
    'Feb': 'February',
    'Mar': 'March',
    'Apr': 'April',
    'May': 'May',
    'Jun': 'June',
    'Jul': 'July',
    'Aug': 'August',
    'Sep': 'September',
    'Oct': 'October',
    'Nov': 'November',
    'Dec': 'December',
    1: 'I am also a key'
}

print(month_conversions.get('SDAOPK', 'Not a valid key'))
print(month_conversions['Nov'])
print(month_conversions[1])
