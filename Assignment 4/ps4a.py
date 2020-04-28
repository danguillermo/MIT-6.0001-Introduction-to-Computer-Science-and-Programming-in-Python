# Problem Set 4A
# Name: Daniel Guillermo
# Collaborators: Daniel Guillermo
# Time Spent: Bout two hours 

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    if len(sequence) == 1:
        return [sequence]
    else:
        ans= []
        for i in range(len(sequence)):
            perms = get_permutations(sequence.replace(sequence[i],''))
            for words in perms:
                ans += [ sequence[i] + words ]
        
        return ans
    #pass #delete this line and replace with your code here

if __name__ == '__main__':
    #EXAMPLE
    example_input = 'abc'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input))
    
    example_input = '123'
    print('Input:', example_input)
    print('Expected Output:', ['123', '132', '213', '231', '312', '321'])
    print('Actual Output:', get_permutations(example_input))
    
    example_input = 'car'
    print('Input:', example_input)
    print('Expected Output:', ['car', 'cra', 'acr', 'arc', 'rac', 'rca'])
    print('Actual Output:', get_permutations(example_input))
    
    # Put three example test cases here (for your sanity, limit your inputs
    # to be three characters or fewer as you will have n! permutations for a 
    # sequence of length n)

    #pass #delete this line and replace with your code here

def get_permutations_test(permutations_list):
    '''
    Tests to see if all elements in permutations_list are different from each
    other.
    
    permutations_list (list of strings): an output list from get_permutations
    that all permutations of a given string
    
    returns boolean, true if no elemets repeat in list, false otherwise
    '''
    
    for word in permutations_list:
        C_list = permutations_list.copy()
        C_list.remove(word)
        for j in C_list:
            if word == j:
                return False
    return True