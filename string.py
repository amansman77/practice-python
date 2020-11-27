if __name__ == '__main__':
    word = '1_20200602_133422.bin'
  
    # returns first occurrence of Substring 
    print ("index:", word[:word.find('.bin')])
    print ("index:", word[word.find('_')+1:word.find('.bin')])