package main

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
	"strconv"
)

type InputLine struct {
	onOff      bool
	dimensions [3][2]int
}

func a2i(in string) int {
	n, e := strconv.Atoi(in)
	if e != nil {
		fmt.Println("Error parsing", e, in)
		return 0
	}
	return n

}

func parseLine(line string) {
	line = "on x=-3..43,y=-40..7,z=-4..40"
	r := regexp.MustCompile(`([^ ]+)` +
		` x=([-0-9]+)\.\.([-0-9]+)` +
		`,y=([-0-9]+)\.\.([-0-9]+)` +
		`,z=([-0-9]+)\.\.([-0-9]+)` +
		`.*`)
	allSubmatches := r.FindAllStringSubmatch(line, -1)
	fmt.Println(allSubmatches[0][0])

	n1 := a2i(allSubmatches[0][2])
	n2 := a2i(allSubmatches[0][3])
	n3 := a2i(allSubmatches[0][4])
	n4 := a2i(allSubmatches[0][5])
	n5 := a2i(allSubmatches[0][6])
	n6 := a2i(allSubmatches[0][7])

	il := InputLine{
		allSubmatches[0][1] == "on",
		[3][2]int{
			{n1, n2},
			{n3, n4},
			{n5, n6}}}

	fmt.Println(il)

}

func main() {

	parseLine("")
	return

	file, err := os.Open("day22.txt")
	if err != nil {
		fmt.Println("Ooops", err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		fmt.Println(scanner.Text())
	}

}
