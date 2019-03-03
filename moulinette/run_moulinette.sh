#! /bin/bash

declare -A exercises=( ["biggest"]="0" ["biggest_advanced"]="1" ["longest_words"]="2" ["my_range"]="3" ["print_first_line"]="4" ["print_first_line_better"]="5" ["hello"]="6" ["print_first_bytes"]="7")

firstname=$(echo $1 | tr '[:upper:]' '[:lower:]')
lastname=$(echo $2 | tr '[:upper:]' '[:lower:]')
exercise_name=$3
exercise_number=${exercises[$exercise_name]}

echo Running moulinette for exercise $exercise_name for student ${firstname}_${lastname}
mkdir -p extracted_dir && tar -x --file=rendus/${firstname}_${lastname}.tar.bz2 --preserve-permissions --same-owner -C extracted_dir/

dir_student_exercice=/extracted_dir/subject/exercises/exercise-$exercise_number/
dir_sandbox=/sandbox/exercise-$exercise_number/

cp $dir_student_exercice/$exercise_name.py $dir_sandbox
[ -e $dir_student_exercice/README ] && cp $dir_student_exercice/README $dir_sandbox
[ -e $dir_student_exercice/README.txt ] && cp $dir_student_exercice/README.txt $dir_sandbox

cd $dir_sandbox
#ls -lR $dir_student_exercices
[ -e README ] && cat README
[ -e README.txt ] && cat README.txt

echo -ne "\n\n==========\nRunning init script.\n\n"
source init_script.sh

for test_file in test_*.sh
do
	[ -e "$test_file" ] || continue
	echo Running $test_file.
	source $test_file
	echo -ne "\n"
done
