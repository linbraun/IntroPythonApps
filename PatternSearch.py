import re

lorem_ipsum = '''Lorem ipsum dolor sit-amet, consectetur adipiscing elit. Phasellus iaculis velit ac nunc interdum tempor. 
Ut volutpat elit metus, vel auctor enim commodo at. Nunc quis quam non ligula ultricies luctus porta id justo. 
Quisque dapibus est ut sagittis bibendum. Mauris ullamcorper pellentesque porttitor. Ut sit:amet ex nec dolor gravida 
porttitor. Proin at justo finibus justo vestibulum congue. Suspendisse et ipsum et ipsum eleifend dapibus a fermentum 
lacus. Vivamus porta nunc eu nisl sagittis, quis vulputate metus dignissim. Integer non fermentum nisl, id vestibulum 
elit. Sed euismod vestibulum purus ut porttitor. Integer sit-amet mollis neque. Donec sed lacinia diam, ac finibus 
lectus. Mauris tempor ipsum nisl, vitae posuere est lacinia nec. Nam eget euismod odio.'''

# Search for special characters and wildcards in lorem_ipsum
results = re.findall('[^\w\d]',lorem_ipsum) 
print(len(results)) # Outputting number of non-alphanumeric character occurrences

# Search for literal characters in lorem_ipsum
occurrance_sit_amet = re.findall('sit[-:]amet',lorem_ipsum)
print(len(occurrance_sit_amet)) # Outputting number of sit-amet and sit:amet occurrences

# Replace sit:amet and sit-amet with sit amet by searching for sequences and ranges
replace_results = re.sub('sit[-:]amet','sit amet',lorem_ipsum)
occurrance_sit_amet = re.findall('sit amet',replace_results)
print(len(occurrance_sit_amet)) # Outputting number of sit amet occurrences