RULES_INPUT = 'rules.txt'
UPDATES_INPUT = 'updates.txt'


def get_rules(rules_path: str) -> list[tuple[str, str]]:
    """Read rules.txt and put them into a list of tuples."""
    with open(rules_path, 'r') as handle:
        rules = handle.readlines()

    rules_list = []
    for rule in rules:
        first, second = rule.strip().split('|')
        rules_list.append((first, second))

    return rules_list


def get_updates(updates_path: str) -> list[list[str]]:
    """Read updates.txt and put them into a list of lists."""
    with open(updates_path, 'r') as handle:
        updates = handle.readlines()

    updates_list = []
    for update in updates:
        updates_list.append(update.strip().split(','))

    return updates_list


def is_update_valid(update: list[str], rules: list[tuple[str, str]]) -> bool:
    """Check if the given update is valid based on the rules."""
    # Filter rules to only include those relevant to the current update
    relevant_rules = [(a, b) for a, b in rules if a in update and b in update]

    # Check each rule
    for a, b in relevant_rules:
        if update.index(a) > update.index(b):
            return False

    return True


def validate_updates(rules: list[tuple[str, str]], updates: list[list[str]]) -> list[list[str]]:
    """Validate each update and return a list of valid updates."""
    return [update for update in updates if is_update_valid(update, rules)]


def sum_middle_number(update_list: list[list[str]]) -> int:
    """For each update get the number in the middle and add to a list, then sum the list."""
    middle_numbers = []
    for update in update_list:
        middle_index = len(update) // 2
        middle_numbers.append(int(update[middle_index]))

    return sum(middle_numbers)


def topological_sort(update: list[str], rules: list[tuple[str, str]]) -> list[str]:
    """Order the pages in the update according to the rules."""
    # Create a dictionary to count how many pages each page depends on
    dependency_count = {page: 0 for page in update}

    # Track which pages depend on others
    dependency_map = {page: [] for page in update}

    # Populate dependencies
    for a, b in rules:
        if a in update and b in update:
            dependency_count[b] += 1
            dependency_map[a].append(b)

    # Start with pages that have no dependencies
    sorted_order = []
    no_dependency = [page for page, count in dependency_count.items() if count == 0]

    while no_dependency:
        current = no_dependency.pop(0)  # Take a page with no dependencies
        sorted_order.append(current)

        # Remove its influence on other pages
        for dependent in dependency_map[current]:
            dependency_count[dependent] -= 1
            if dependency_count[dependent] == 0:
                no_dependency.append(dependent)

    return sorted_order



def find_and_correct_invalid_updates(rules: list[tuple[str, str]], updates: list[list[str]]) -> list[list[str]]:
    """Find invalid updates, correct their order, and return them."""
    corrected_updates = []

    for update in updates:
        if not is_update_valid(update, rules):
            corrected_updates.append(topological_sort(update, rules))

    return corrected_updates


def main():
    rules = get_rules(RULES_INPUT)
    updates = get_updates(UPDATES_INPUT)

    # Get valid and corrected invalid updates
    valid_updates = validate_updates(rules, updates)
    corrected_invalid_updates = find_and_correct_invalid_updates(rules, updates)

    # Compute sums
    valid_sum = sum_middle_number(valid_updates)
    invalid_sum = sum_middle_number(corrected_invalid_updates)

    print(f"Sum of middle numbers from valid updates: {valid_sum}.")
    print(f"Sum of middle numbers from corrected invalid updates: {invalid_sum}.")


if __name__ == '__main__':
    main()
