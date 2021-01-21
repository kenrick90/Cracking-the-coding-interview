#Phone Number and Email Address Extractor
import pyperclip, re

phoneRegex = re.compile(r'''(
 (\d{3}|\(\d{3}\))? # area code
 (\s|-|\.)? # separator
 (\d{3}) # first 3 digits
 (\s|-|\.) # separator
 (\d{4}) # last 4 digits
 (\s*(ext|x|ext.)\s*(\d{2,5}))? # extension
 )''', re.VERBOSE)

emailRegex = re.compile(r'''(
	[a-zA-Z0-9._%+-]+ # prefix
	@
	[a-zA-Z0-0.-]+
	(\.[a-zA-Z]{2,4})
	)''', re.VERBOSE)


# TODO: Create email regex.
# TODO: Find matches in clipboard text.
text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
# TODO: Copy results to the clipboard.