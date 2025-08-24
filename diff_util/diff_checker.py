from rich import print


def check_differences(original_contents, changed_contents):
    """Check and print the differences between two lists of file contents."""
    color = "green"
    symbol = f"[bold {color}][+]"

    # Determine which file has changed much.
    if len(changed_contents) <= len(original_contents):
        color = "red"
        symbol = f"[bold {color}][-]"
        smallest_sloc, largest_sloc = changed_contents, original_contents
    else:
        smallest_sloc, largest_sloc = original_contents, changed_contents

    # Go over all the lines to check the changes.
    for line in range(0, len(smallest_sloc)):
        if original_contents[line] == changed_contents[line]:
            # Ignore if the lines are same.
            continue
        else:
            # Display the changes on the respective lines of the files.
            print(f"[bold red][-] Line {line + 1}:[/bold red] {original_contents[line]}", end="")
            print(f"[bold green][+] Line {line + 1}:[/bold green] {changed_contents[line]}")

            # Show the additions [+] or deletions [-] for the file that is the largest.
            if line == len(smallest_sloc) - 1:
                for new_line in range(line + 1, len(largest_sloc)):
                    print(f"{symbol} Line {new_line + 1}:[/bold {color}] {largest_sloc[new_line]}")
