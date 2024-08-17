# Full transaction python - Working
TRANSACTION = r"###\n(?P<date>\d{2} \w* \d{4})\n(?P<valuedate>\d{2} \w* \d{4})\n(?P<description>[^#]*)###\n(?P<transaction>[0-9,]*\.[0-9]*)\n(?P<balance>[0-9,]*\.[0-9]*)"

# balance forward python - Working
BALANCE_FORWARD = r"###\n(?P<date>\d{2} \w* \d{4})\n(?P<valuedate>\d{2} \w* \d{4})\nBALANCE FORWARD\n(?P<balance>[0-9,]*\.[0-9]*)"

# total python - Working
TOTAL = r"Total\n(?P<deposit>[0-9,]*\.[0-9]*)\n(?P<withdrawal>[0-9,]*\.[0-9]*)\n(?P<balance>[0-9,]*\.[0-9]*)"

PASSWORD = ""
