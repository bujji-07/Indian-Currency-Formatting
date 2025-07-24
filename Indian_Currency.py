def format_indian_currency(num):
    s = str(num)
    if '.' in s:
        int_part, dec_part = s.split('.')
        dec_part = '.' + dec_part
    else:
        int_part = s
        dec_part = ''

    if len(int_part) <= 3:
        return int_part + dec_part

    last_three = int_part[-3:]
    remaining = int_part[:-3]
    parts = []
    
    while len(remaining) > 2:
        parts.insert(0, remaining[-2:])
        remaining = remaining[:-2]

    if remaining:
        parts.insert(0, remaining)
    
    return ','.join(parts + [last_three]) + dec_part


print(format_indian_currency(123456.7891))  
