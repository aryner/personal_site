import sys

def addMeta(lines,index,data,cat):
  data[cat] = lines[index+1]
  data['%s_link'%cat] = lines[index+2]
  return index + 3
  
def addSpeaker(lines,index,data):
  if 'speakers' not in data:
    data['speakers'] = {'1':lines[index+1]}
    data['speakers']['1_link'] = lines[index+2]

  else:
    s_num = 1
    while str(s_num) in data['speakers']:
      s_num += 1
    data['speakers'][str(s_num)]  = lines[index+1]
    data['speakers']['%d_link'%s_num] = lines[index+2]

  return index + 3

def addSection(lines,index,data):
  section = {'title':lines[index+1]}
  index += 2
  tag, index = getTag(lines,index)

  index = buildSection(lines,tag,index,section)

  if 'content' not in data:
    data['content'] = {'1':section}
  else:
    i = 1
    while str(i) in data['content']:
      i += 1
    data['content'][str(i)] = section

  return index

def buildSection(lines,tag,index,section):
  i = 1
  while str(i) in section:
    i += 1

  if tag == 'end':
    return index
  elif tag == 'subsection':
    sub = {'title':lines[index]}
    index += 1
    tag,index = getTag(lines,index)
    index = buildSection(lines,tag,index,sub)
    section[str(i)] = sub
  else:
    startIndex = index
    while (tag == 'pre' and lines[index] != '#ENDCODE') or (len(lines[index]) > 0 and lines[index][0] != '#'):
      index += 1
    content = ''
    for j in range(startIndex,index):
      if content and tag == 'p':
        content = '%s<br><br>%s'%(content,lines[j])
      elif content:
        content = '%s<br>%s'%(content,lines[j])
      else:
        content = lines[j]
    block = {'tag':tag,'content':content}
    section[str(i)] = block

  tag,index = getTag(lines,index)
  return buildSection(lines,tag,index,section)
  
# returns the tag to use and the index of where that tag starts
def getTag(lines,index):
  line = lines[index]
  if line == '#SECTION' or line == '':
    return 'end',index
  elif line == '#ENDSUB':
    return 'end',index+1
  elif line == '#SUBSECTION':
    return 'subsection',index+1
  elif line == '#CODE':
    return 'pre',index+1
  elif line == '#ENDCODE':
    return getTag(lines,index+1)
  else:
    return 'p',index

def switch(lines,index,data):
  if lines[index] == '#TITLE':
    return addMeta(lines,index,data,'title')
  if lines[index] == '#SUBTITLE':
    return addMeta(lines,index,data,'subtitle')
  if lines[index] == '#SPEAKER':
    return addSpeaker(lines,index,data)
  if lines[index] == '#LOCATION':
    return addMeta(lines,index,data,'location')
  if lines[index] == '#SECTION':
    return addSection(lines,index,data)
  else:
    return index+1

def getLines(name):
  f = open(sys.argv[1],'r')
  lines = []
  line = f.readline()
  while line != '':
    lines.append(line.rstrip('\n'))
    line = f.readline()

  f.close()
  return lines

def transformToJson(lines):
  data = {}
  index = 0
  while index < len(lines)-1:
    index = switch(lines,index,data)

  return data

if __name__ == '__main__':
  lines = getLines(sys.argv[1])
  data = transformToJson(lines)

  print(data)


