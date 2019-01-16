#!/usr/bin/python -tt

import sys, getopt, string, time, webbrowser, requests, random

word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"

response = requests.get(word_site)
word_list = response.content.splitlines()
random.choice(word_list)

email = random.choice(word_list)

domain = random.choice(word_list)

def main(argv):
  first = ''
  last = ''
  try:
    opts, args = getopt.getopt(argv,"F:L:",["first=","last="])
  except getopt.GetoptError:
    print('99s.py -F <First_Name> -L <Last_Name>')
    sys.exit(2)
  for opt, arg in opts:
    if opt in ("-F", "first"):
      first = arg
    elif opt in ("-L", "last"):
      last = arg
  date = (time.strftime("%m/%d/%Y"))
  url = "http://www.99restaurants.com/coupons/coupon_welcome.php?name=%s&lname=%s&email=%s@%s.com&exp=%s" % (first, last, email, domain, date)
  if len(first) > 1:
      if len(last) > 1:
        webbrowser.open_new(url)
      else:
        print('99s.py -F <First_Name> -L <Last_Name>')
  else:
    print('99s.py -F <First_Name> -L <Last_Name>')

if __name__ == '__main__':
    main(sys.argv[1:])
