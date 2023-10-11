def encrypt(message, stride=1):
    sliced_message = ""
    for starting_index in range(stride):
        sliced_message += message[starting_index::stride]

    encrypted_message = ""
    for index in range(len(sliced_message)):
        encrypted_message += chr(ord(sliced_message[index]) + index)

    return encrypted_message


"""
GPT prompt:
how do you reverse this function
def encrypt(message, stride=1):
    sliced_message = ""
    for starting_index in range(stride):
        sliced_message += message[starting_index::stride]

    encrypted_message = ""
    for index in range(len(sliced_message)):
        encrypted_message += chr(ord(sliced_message[index]) + index)

    return encrypted_message
"""
def decrypt_gpt(encrypted_message, stride=1):
    sliced_message = ""
    for index in range(len(encrypted_message)):
        sliced_message += chr(ord(encrypted_message[index]) - index)

    length = len(sliced_message)
    group_size = (length + stride - 1) // stride  # Ceiling division
    parts = [sliced_message[i::group_size] for i in range(group_size)]

    message = ""
    for i in range(group_size):
        for part in parts:
            try:
                message += part[i]
            except IndexError:
                pass  # Some parts might be shorter than others

    return message

def decrypt(message, stride=1):
    chunked_message = ""
    for index in range(len(message)):
        chunked_message += chr(ord(message[index]) - index)

    print(chunked_message)

    original_message = ""

    chunk_length = len(message) // stride
    number_of_longer_chunks = len(message) % stride

    for character_index_in_chunk in range(chunk_length):
        chunk_number = 0
        index = character_index_in_chunk
        while index < len(chunked_message):
            original_message += chunked_message[index]
            index += chunk_length
            if chunk_number < number_of_longer_chunks:
                index += 1
            chunk_number += 1

    index = chunk_length
    for remaining_character in range(number_of_longer_chunks):
        original_message += chunked_message[index]
        index += chunk_length + 1

    return original_message


encrypted_message = encrypt("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 3)
print(encrypted_message)
print(decrypt(encrypted_message, 3))
print(decrypt_gpt(encrypted_message, 3))
