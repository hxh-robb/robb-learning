#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
# import pdb

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def extract_year(text):
  ''' extract year '''
  match = re.search(r'Popularity in (\d+)', text)
  return match.group(1)
  # return re.findall(r'Popularity in (\d+)', text)

def extract_name_rank(text):
  ''' extract name rank pair '''
  nrs = re.findall(r'<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>', text)
  # rt_list = []
  # for name_rank in nrs:
  #   rt_list.append('%s %s' % (name_rank[1], name_rank[0])) # Male baby name
  #   rt_list.append('%s %s' % (name_rank[2], name_rank[0])) # Female baby name
  nr_dict = {}
  for name_rank in nrs:
    # if('Adrian' in name_rank):
    #   pdb.set_trace()
    if name_rank[1] not in nr_dict:
      nr_dict[name_rank[1]] = int(name_rank[0])
    if name_rank[2] not in nr_dict:
      nr_dict[name_rank[2]] = int(name_rank[0])
    # nr_dict[name_rank[1]] = int(name_rank[0])
    # nr_dict[name_rank[2]] = int(name_rank[0])
  nr_list = []
  for nr_tuple in nr_dict.iteritems():
    nr_list.append('%s %d' % nr_tuple)
  return nr_list

def extract_names(file_name):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  try:
    file_content = ''
    rt_list = []
    with open(file_name) as input_file:
      file_content = input_file.read()
    rt_list.append(extract_year(file_content))
    rt_list.extend(extract_name_rank(file_content))
    return sorted(rt_list)
  except IOError:
    pass

def print_names(name_rank_list):
  print '\n'.join(name_rank_list)

def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print 'usage: [--summaryfile] file [file ...]'
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  # file_list = []
  # for file_names in args:
  #   for file_name in glob.iglob(file_names):
  #     if file_name in file_list:
  #       continue
  #     file_list.append(file_name)
  #     if summary:
  #       with open(file_name + '.summary', 'w') as summary_file:
  #         print >> summary_file, extract_names(file_name)
  #     else:
  #       print extract_names(file_name)

  for file_name in args:
    print_names(extract_names(file_name))
if __name__ == '__main__':
  main()
  # extract_names(sys.argv[1])
