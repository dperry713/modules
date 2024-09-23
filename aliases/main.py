# main.py

# Import text_utils using an alias
import text_utils as tu

if __name__ == "__main__":
    sample_text = "hello world"

    # Utilize functions from text_utils
    reversed_text = tu.reverse_string(sample_text)
    capitalized_text = tu.capitalize_string(sample_text)

    print("Reversed:", reversed_text)  # Output: "dlrow olleh"
    print("Capitalized:", capitalized_text)  # Output: "Hello world"
