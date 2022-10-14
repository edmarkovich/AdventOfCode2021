package main

import (
	"fmt"
	"math"
)

var die_next, score1, score2, pos1, pos2, rolls int

func next_die() int {
	die_next++
	if die_next == 101 {
		die_next = 1
	}
	rolls++
	return die_next
}

func next_3() int {
	var x = next_die() + next_die() + next_die()
	return x
}

func next_place(start int) int {
	var x = start + next_3()
	for x > 10 {
		x -= 10
	}
	return x
}

func mainY() {

	//main2()
	return

	pos1 = 4
	pos2 = 8

	for {
		pos1 = next_place(pos1)
		score1 += pos1
		if score1 >= 21 {
			break
		}
		//fmt.Println("1:", pos1, score1)

		pos2 = next_place(pos2)
		score2 += pos2
		if score2 >= 21 {
			break
		}
		//fmt.Println("2:", pos2, score2)

	}

	fmt.Println("Hello, World!", score1, score2, rolls, int(math.Min(float64(score1), float64(score2))*float64(rolls)))
}
