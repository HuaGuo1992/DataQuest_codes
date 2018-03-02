## 2. Extract Line Numbers ##

raw_hamlet = sc.textFile("hamlet.txt")
split_hamlet = raw_hamlet.map(lambda line: line.split('\t'))
split_hamlet.take(5)


def func(line):
    line[0] = line[0].replace('hamlet@', '')
    return line

hamlet_with_ids = split_hamlet.map(func)
hamlet_with_ids.take(3)

## 3. Remove Blank Values ##

hamlet_with_ids.take(5)
def text_only_filter(line):
    if len(line) <= 1:
        return False
    return True
    
def text_only_map(line):    
    return [l for l in line if l!='']

hamlet_text_only = hamlet_with_ids.filter(text_only_filter).map(text_only_map)    
hamlet_text_only.take(10)

## 4. Remove Pipe Characters ##

hamlet_text_only.take(10)
clean_hamlet = hamlet_text_only.map(lambda line: [l.replace('|', '') for l in line if l!='|'])
clean_hamlet.take(20)