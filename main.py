# Part 1
def read_csv(filename):
    # Type your code below
  """
  Open file

  strip & split

  header

  """
  header = []
  data = []

  with open(filename, 'r') as text:
    header = text.readline().strip().split(",")

    for line in text:
        new_line = line.strip().split(",")
        new_line[0] = int(new_line[0])
        new_line[3] = int(new_line[3])
        data.append(new_line)

    return header, data


# Part 2
def filter_gender(enrolment_by_age, sex):
    # Type your code below
    """
    filter by sex
    exclude sex
    """
    filtered = []

    for line in enrolment_by_age:
      if line[2] == sex:
        filtered.append([line[0], line[1], line[3]])

    return filtered


# Part 3
def sum_by_year(enrolment):
    # Type your code below
    """
    Only return year and sum
    Make a counter for each year

    """
    # man i cannot debug this
    """

    no_year = []
    total_enrolment = []

    for data in enrolment:
      year = data[0]
      if year not in no_year:
        total_enrolment[year] = data[-1]
        no_year.append(year)
      else:
        total_enrolment[year] = total_enrolment[year] + data[-1]

    for year in no_year:
      no_year.append([year, total_enrolment[year]])

    return no_year
     """

    #straight forward 🙂
    total_enrolment = []

    for year in range(35):
      total_enrolment.append([1984+year, 0])
      for line in enrolment:
        if line[0] == 1984+year:
          total_enrolment[year][1] += line[-1]

    return total_enrolment


# Part 4
def write_csv(filename, header, data):
    # Type your code below
    """
    write header n data to filename
    same format.-.
    counter for number of lines
    """
    count = 0
    with open(filename, 'w') as new_file:
      new_file.writelines(header)

      for line in data:
        line[0] = str(line[0])
        line[1] = str(line[1])
        new_file.writelines(",".join(line))
        count = count + 1

    new_file.close()
    return count


# TESTING
# You can write code below to call the above functions
# and test the output
