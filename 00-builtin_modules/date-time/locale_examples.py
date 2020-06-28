import locale
from datetime import datetime

# locale converted day month names
locale.setlocale(locale.LC_ALL, "")
datetime.strftime(datetime.now(), "%Y/%B/%A")

# get current locale
loc = locale.getlocale()  
