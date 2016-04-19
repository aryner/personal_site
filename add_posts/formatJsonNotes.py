def getSections(contentJson):
  sections = []
  index = 1

  while str(index) in contentJson:
    sections.append(contentJson[str(index)])
    index += 1

  return sections

def format_title(title,h=3):
  return '<h%d>%s</h%d>'%(h,title,h)

def format_tag(section):
  return '<%s>%s</%s>'%(section['tag'],section['content'],section['tag'])

def format_section(section,nested=False):
  content = format_title(section['title'], 4 if nested else 3)

  subsections = getSections(section)
  
  for subsection in subsections:
    if 'title' in subsection:
      content = '%s%s'%(content,format_section(subsection,True))
    else:
      content = '%s%s'%(content,format_tag(subsection))

  return content

def format_content(json):
  content = ''
  contentJson = json['content']
  sections = getSections(contentJson)

  for section in sections:
    content = '%s%s'%(content,format_section(section))

  return content

if __name__ == '__main__':
  import sys
  import ast

  name = sys.argv[1]
  f = open(name,'r')
  jsonString = f.readline()
  json = ast.literal_eval(jsonString)
  f.close()
  content = format_content(json)
  print(content)
  

