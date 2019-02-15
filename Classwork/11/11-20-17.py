def main():
        in_file = open("grades.csv", "r")
        out_file = open("final grades.csv", "w")

        in_file.readline()
        print("NYU ID, Final Grade", file = out_file)
        for line in in_file:
            curr_lst = line.split(',')
            NYU_ID = curr_lst[0]
            midterm1 = int(curr_lst[1])
            midterm2 = int(curr_lst[2])
            final = int(curr_lst[3])
            homework = int(curr_lst[4])
            lab = int(curr_lst[5])
            participation = int(curr_lst[6])

            grade = calc_grade(midterm1, midterm2, final, homework, lab, participation)
            print(NYU_ID, grade, sep=',', file = out_file)

    def calc_grade(midterm1, midterm2, final, homework, lab, participation):
        exam_lst = [midterm1, midterm2, final]
        exam_lst.sort()
        grade = 0.15*exam_lst[0] + 0.2*exam_lst[1] + 0.25*exam_lst[2] + 0.2*homework + 0.2*lab + 0.05*participation
        return round(grade)

main()
