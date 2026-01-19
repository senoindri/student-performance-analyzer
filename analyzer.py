import csv

def percentage(marks, total):
    return (marks / total) * 100

def percentage_to_grade_point(percent):
    if percent >= 90:
        return 10
    elif percent >= 80:
        return 9
    elif percent >= 70:
        return 8
    elif percent >= 60:
        return 7
    elif percent >= 50:
        return 6
    else:
        return 0

def read_data(filename):
    subjects = []
    with open(filename, newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row['Credits'] = int(row['Credits'])
            row['Marks'] = int(row['Marks'])
            row['TotalMarks'] = int(row['TotalMarks'])

            percent = percentage(row['Marks'], row['TotalMarks'])
            row['Percentage'] = round(percent, 2)
            row['GradePoint'] = percentage_to_grade_point(percent)

            subjects.append(row)
    return subjects

def calculate_cgpa(subjects):
    total_points = 0
    total_credits = 0

    for s in subjects:
        total_points += s['GradePoint'] * s['Credits']
        total_credits += s['Credits']

    return round(total_points / total_credits, 2)

def performance_summary(subjects):
    best = max(subjects, key=lambda x: x['Percentage'])
    worst = min(subjects, key=lambda x: x['Percentage'])
    return best['Subject'], worst['Subject']

def main():
    data = read_data("data/sample_marks.csv")
    cgpa = calculate_cgpa(data)
    best, worst = performance_summary(data)

    print("----- Student Performance Report -----")
    print(f"CGPA: {cgpa}")
    print(f"Strongest Subject: {best}")
    print(f"Weakest Subject: {worst}")

    print("\nSubject-wise Details:")
    for s in data:
        print(
            f"{s['Subject']}: "
            f"{s['Marks']}/{s['TotalMarks']} "
            f"({s['Percentage']}%)"
        )

if __name__ == "__main__":
    main()
