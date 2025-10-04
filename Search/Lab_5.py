def can_partition(lessons, max_allowed_sum):
    periods_needed = 1
    current_sum = 0
    for lesson_time in lessons:
        if current_sum + lesson_time <= max_allowed_sum:
            current_sum += lesson_time
        else:
            periods_needed += 1
            current_sum = lesson_time
    return periods_needed

def solve_class_schedule(lessons, periods):
    low = max(lessons) if lessons else 0
    high = sum(lessons) if lessons else 0
    min_max_period = high
    while low <= high:
        mid = (low + high) // 2
        periods_required = can_partition(lessons, mid)
        if periods_required <= periods:
            min_max_period = mid
            high = mid - 1
        else:
            low = mid + 1
    return min_max_period

def get_groups(lessons, period, max_period):
    n = len(lessons)
    groups = []
    current_group = []
    current_sum = 0

    for i, lesson_time in enumerate(lessons):
        current_group.append(lesson_time)
        current_sum += lesson_time
        is_last_lesson = (i == n - 1)
        next_lesson_exceeds = False
        if not is_last_lesson:
            if current_sum + lessons[i + 1] > max_period:
                next_lesson_exceeds = True
        split_for_period = False
        remaining_lessons = n - (i + 1)
        remaining_groups_to_form = period - (len(groups) + 1)
        if remaining_lessons == remaining_groups_to_form:
            split_for_period = True
        if is_last_lesson or next_lesson_exceeds or split_for_period:
            groups.append(current_group)
            current_sum = 0
            current_group = []
    group_sums = [sum(g) for g in groups]
    return groups, group_sums

print("*** CLASS SCHEDULE ***")
lessons , periods = input("Lesson times / periods: ").split(" / ")
lessons = list(map(int,lessons.split()))
periods = int(periods)
max_period = solve_class_schedule(lessons, periods)
print(f"Max period: {max_period}")
groups, group_sums = get_groups(lessons, periods, max_period)
diff = max(group_sums) - min(group_sums) if group_sums else 0
print(f"Diff: {diff}")
print("Groups:")
for i, group in enumerate(groups):
    print(f"  Group {i+1}: {group} → sum = {group_sums[i]}")