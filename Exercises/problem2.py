#Problem 2: String Compression

def stringCompr(string):
    compressed_string = []
    count = 1

    for pos in range(1,len(string)):
        print(string[pos])
        if string[pos] == string[pos-1]:
            count = count+1
        else:
            compressed_string.append(f"{string[pos-1]}{count}") 
            count = 1
    
    #print(compressed_string)
    compressed_string.append(f"{string[-1]}{count}")
    #print(compressed_string)
    compressed_string=''.join(compressed_string)

    return print(compressed_string)


word = "aabcccccaaabb"
stringCompr(word)





'''Description: Implement a function to perform basic string 
compression using the counts of repeated characters. 
For example, "aabcccccaaa" becomes "a2b1c5a3".

Requirements:
  Input: A string
  Output: Compressed string
Example: 
  Input: `"aaabbcccc"`
 Output: `"a3b2c4"` 
'''