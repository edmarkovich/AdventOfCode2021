package main

import (
	"bufio"
	"fmt"
	"math"
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

func parseLine(line string) InputLine {
	r := regexp.MustCompile(`([^ ]+)` +
		` x=([-0-9]+)\.\.([-0-9]+)` +
		`,y=([-0-9]+)\.\.([-0-9]+)` +
		`,z=([-0-9]+)\.\.([-0-9]+)` +
		`.*`)
	allSubmatches := r.FindAllStringSubmatch(line, -1)

	n1 := a2i(allSubmatches[0][2])
	n2 := a2i(allSubmatches[0][3])
	n3 := a2i(allSubmatches[0][4])
	n4 := a2i(allSubmatches[0][5])
	n5 := a2i(allSubmatches[0][6])
	n6 := a2i(allSubmatches[0][7])

	return InputLine{
		allSubmatches[0][1] == "on",
		[3][2]int{
			{n1, n2},
			{n3, n4},
			{n5, n6}}}
}

func isInBounds(il InputLine) bool {
	for i := 0; i < 3; i++ {
		for j := 0; j < 2; j++ {
			if math.Abs(float64(il.dimensions[i][j])) > 50.0 {
				return false
			}
		}

	}
	return true
}

var cubeMap map[Key]bool

type Key struct {
	x, y, z int
}

func updateMap(il InputLine) {
	for i := il.dimensions[0][0]; i <= il.dimensions[0][1]; i++ {
		for j := il.dimensions[1][0]; j <= il.dimensions[1][1]; j++ {
			for k := il.dimensions[2][0]; k <= il.dimensions[2][1]; k++ {
				key := Key{i, j, k}
				if il.onOff {
					cubeMap[key] = true
				} else {
					if _, ok := cubeMap[key]; ok {
						delete(cubeMap, key)
					}
				}
			}
		}
	}
}

func main() {

	cubeMap = make(map[Key]bool)

	file, err := os.Open("day22.txt")
	if err != nil {
		fmt.Println("Ooops", err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)

	for scanner.Scan() {
		il := parseLine(scanner.Text())
		if !isInBounds(il) {
			continue
		}
		updateMap(il)
	}

	fmt.Println(len(cubeMap))

}
