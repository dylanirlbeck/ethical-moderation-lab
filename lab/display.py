from beautifultable import BeautifulTable

def display_training_data(arr):
    """
    Precondition: each element in `arr` is a tuple:
        (valid, title)
    Where valid is 'y'/'n' representing a valid/invalid post (respectively), and title is the title of the submission.
    """
    table = BeautifulTable(max_width = 79)
    table.columns.header = [
        "Valid?", "Title of post submission"
    ]
    for entry in arr:
        table.rows.append(entry)
    print(table)
print("lab.display imported!")