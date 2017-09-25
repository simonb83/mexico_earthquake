### Script credited to: http://journal.code4lib.org/articles/11358

import sys
import json
import fileinput
import dateutil.parser
import dateutil.rrule
import pytz
import pandas as pd
import datetime
import io
 
eastern = pytz.timezone('US/Eastern')
start_date = dateutil.parser.parse("19-September-2017")
start_date = eastern.localize(start_date)
end_date = dateutil.parser.parse("21-September-2017")
end_date = eastern.localize(end_date)
 
dates = pd.date_range(start_date, end_date).tolist()
 
for date in dates:
    date_plus_one = date + pd.DateOffset(1)
    pretty_print = date.to_pydatetime().strftime('%Y%m%d')
    filename = 'data/processed/account_tweets' + pretty_print + '.json'
    f = io.open(filename, 'w', encoding='utf-8')
 
    for line in fileinput.input():
        tweet = json.loads(line)
        created_at = dateutil.parser.parse(tweet["created_at"])
        created_at = created_at.astimezone(eastern)
        if ((created_at >= date) and (created_at < date_plus_one)):
            f.write(json.dumps(tweet, ensure_ascii=False) + '\n')
 
    f.close()