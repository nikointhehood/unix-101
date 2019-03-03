current=$(pwd)
cd ..
docker build -t moulinette .

function go() {
	firstname=$1
	lastname=$2
	results_dir=${current}/traces/${firstname}_${lastname}/
	mkdir -p $results_dir
	for exo in biggest biggest_advanced longest_words my_range print_first_line print_first_line_better hello print_first_bytes
	do
		docker run -e "firstname=$1" -e "lastname=$2" -e "exo_name=$exo" moulinette > ${results_dir}/${exo}.txt
	done
}


go nicolas chariglione
