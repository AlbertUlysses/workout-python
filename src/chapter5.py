""" Code for chapter 5
"""
import os
import re
import csv
import json
from pathlib import Path
from statistics import mean


def get_final_line(file_path: str) -> str:
    """returns the last line of a file."""
    with open(file_path, "r", encoding="utf-8") as f:
        file_content = f.read()
    return file_content.strip().split("\n")[-1]


def passwrd_to_dict(file_path: str) -> dict:
    """Returns a key value pair of usernames and user ids from a passwrd file."""
    with open(file_path, "r", encoding="utf-8") as f:
        file_content = f.read()
    user_name_id_dict = {
        user.split(":")[0]: user.split(":")[2]
        for user in file_content.strip().split("\n")
    }
    return user_name_id_dict


def word_count(file_path: str) -> str:
    """Tells the user how many characters, words, unique words, and lines of a file."""
    with open(file_path, "r", encoding="utf-8") as f:
        file_content = f.read().strip()
    chars_count = len(file_content)
    word_count = len(words := file_content.split())
    unique_words = len(set(words))
    line_count = len(file_content.split("\n"))
    return f"This file has: {chars_count} characters, {word_count} words, {unique_words} unique words, and {line_count} lines"


def find_longest_word(file_path: str) -> str:
    """Returns the longest word in a file."""
    with open(file_path, "r", encoding="utf-8") as f:
        file_content = f.read()
    no_ponctuation_string = re.sub(r"[^\w\s]", "", file_content)
    return max(no_ponctuation_string.split(), key=lambda x: len(x.strip()))


def find_all_longest_words(directory_path: str) -> dict:
    """Takes a directory and returns a dictionary of the longest words."""
    pathlist = Path(directory_path).glob("**/*.txt")
    return {path.name: find_longest_word(str(path)) for path in pathlist}


def passwrd_to_csv(passwrd_file_path: str, output_csv_path: str) -> None:
    """Takes a passwrd_file and returns a csv file that has usernames and ids."""
    with open(passwrd_file_path, "r", encoding="utf-8") as f:
        file_content = f.read().strip()
    with open(output_csv_path, "w") as f:
        csv_write_object = csv.writer(f, delimiter="\t")
        for row in file_content.split("\n"):
            if row[0] != "#":
                row_list = row.split(":")
                csv_write_object.writerow([row_list[0], row_list[2]])


def calculate_score(class_scores: list, subject: str) -> tuple:
    """Takes a list of dicts to returns the min, max, and average of a subject."""
    subject_values = [entry[subject] for entry in class_scores]
    return (min(subject_values), max(subject_values), mean(subject_values))


def print_scores(json_file_path: str) -> None:
    """Prints the min, max, and average of class collection."""
    with open(json_file_path) as file_:
        file_content = json.load(file_)
    for class_subject in file_content[0].keys():
        min_value, max_value, avg_value = calculate_score(
            file_content, str(class_subject)
        )
        print(f"{class_subject}: min {min_value}, max {max_value}, average {avg_value}")


def reverse_lines(input_file_path: str, output_file_path: str) -> None:
    """Reverses each line from the input file_path and adds it to the output file."""
    with open(
        input_file_path, "r", encoding="utf-8"
    ) as file_in, open(
        output_file_path, "w", encoding="utf-8"
    ) as file_out:
        reverse_file_content = [row[::-1] for row in file_in.read().split("\n")]
        file_out.write("\n".join(reverse_file_content))
