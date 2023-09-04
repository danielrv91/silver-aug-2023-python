if __name__ == '__main__':
    # Get the number of commands as input
    N = int(input())
    
    # Initialize an empty list to store values
    values = []
    
    # Loop through the specified number of commands
    for i in range(N):
        instruct = input()
        instructions = instruct.split(' ')
        
        # Check the first word of the input instruction and perform the corresponding operation
        if 'insert' in instructions[0]:
            # Insert an element at the specified index
            values.insert(int(instructions[1]), int(instructions[2]))
        elif 'print' in instructions[0]:
            # Print the current list of values
            print(values)
        elif 'remove' in instructions[0]:
            # Remove the specified element from the list
            values.remove(int(instructions[1]))
        elif 'append' in instructions[0]:
            # Append an element to the end of the list
            values.append(int(instructions[1]))
        elif 'sort' in instructions[0]:
            # Sort the list in ascending order
            values.sort()
        elif 'pop' in instructions[0]:
            # Remove and return the last element from the list
            values.pop()
        elif 'reverse' in instructions[0]:
            # Reverse the order of elements in the list
            values.reverse()
