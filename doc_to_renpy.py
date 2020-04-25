
def read_text_to_renpy(in_file, out_file, who=None):
  previous_name = ""
  # assume delineated by new lines
  with open(in_file, 'r') as fp:
    with open(out_file, "w") as fo:
      for line in fp.readlines():
        # assume dialogue is formatted like this:
        # NAME: dialog
        colon_index = line.find(':')

        # If there isn't a colon, then assume it's an inner thought
        if colon_index == -1:
          name = who if who else "reader"
          dialogue = line[:-1]
        else:
          name = line[:colon_index].strip().lower()
          dialogue = line[colon_index + 1:-1].strip()
        
        # remove non ascii characters:
        dialogue = dialogue.decode("utf-8").replace(u"\u2019", "'")
        dialogue = dialogue.replace(u"\u2026", "...")
        dialogue = dialogue.replace(u"\u201c",'\\"')
        dialogue = dialogue.replace(u"\u201d",'\\"')
        dialogue = dialogue.replace('"', '\\"')
        dialogue = dialogue.replace('%', '\\%')

        if len(dialogue) == 0:
          continue
        out_lines = ''
        if previous_name != name:
          out_lines = '\n'
          previous_name = name
          
        out_lines += '{0} "{1}"\n'.format(name, dialogue)
        fo.write(out_lines)

read_text_to_renpy('test.txt', 'test_out.txt')
