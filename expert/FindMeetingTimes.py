def update_calendar(calendar, daily_bounds):
    updated_calendar = calendar
    before_work_unavailability = ["00:00", daily_bounds[0]]
    after_work_unavailability = [daily_bounds[1], "23:59"]
    updated_calendar.insert(0, before_work_unavailability)
    updated_calendar.append(after_work_unavailability)
    print(updated_calendar)

    # convert to min
    minute_calendar = []
    for timeslot in updated_calendar:
        minute_slots = []
        for times in timeslot:
            minute_slots.append(convert_to_min(times))
        minute_calendar.append(minute_slots)

    print(minute_calendar)


# "10:30" => 630
def convert_to_min(time):
    # list(map(lambda x: int(x), time.split(":")))
    hours, minutes = [int(x) for x in time.split(":")]
    return hours * 60 + minutes


if __name__ == "__main__":
    calendar = [
        ["9:00", "10:30"],
        ["12:00", "13:00"],
        ["16:00", "18:00"]
    ]
    daily_bounds = ["9:00", "20:00"]
    update_calendar(calendar, daily_bounds)
