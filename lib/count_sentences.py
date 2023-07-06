#!/usr/bin/env python3

class MyString:
  def __init__(self, value=''):
    self.value = value

  def get_value(self):
    return self._value
  
  def set_value(self, value):
    if type(value) == str:
      self._value = value
    else:
      print("The value must be a string.")

  def is_sentence(self):
    if self.value[-1] == '.':
      return True
    else:
      return False
    
  def is_question(self):
    if self.value[-1] == '?':
      return True
    else:
      return False
    
  def is_exclamation(self):
    if self.value[-1] == '!':
      return True
    else:
      return False
    
  def count_sentences(self):
    count = 0
    
    for i in range(len(self.value)):
      if self.value[i] in ['.','!','?']:
        if self.value[i - 1] not in ['.','!','?']:
          count += 1

    return count


  value = property(get_value, set_value)