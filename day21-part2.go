package main

import "fmt"

type PlayerState struct {
	pos, score, tosses int
}

type State struct {
	playerStates [2]PlayerState
	onesTurn     bool
}

type WinCount struct {
	wins [2]uint64
}

var m map[State]WinCount

func checkState(s State) WinCount {

	sOrig := s

	if val, ok := m[sOrig]; ok {
		return val
	}

	var whichPlayer int
	if s.onesTurn {
		whichPlayer = 0
	} else {
		whichPlayer = 1
	}

	if s.playerStates[whichPlayer].tosses == 3 {
		// Did I win?
		if s.playerStates[whichPlayer].score >= 21 {
			var wc WinCount
			wc.wins[whichPlayer] = 1
			m[sOrig] = wc

			return wc
		}

		// Now its their turn
		s.playerStates[whichPlayer].tosses = 0
		s.onesTurn = !s.onesTurn
		wc := checkState(s)
		m[sOrig] = wc
		return wc
	} else {
		// Create 3 universes
		s.playerStates[whichPlayer].tosses++

		var out WinCount

		for i := 1; i < 4; i++ {
			s1 := s
			s1.playerStates[whichPlayer].pos += i
			if s1.playerStates[whichPlayer].pos > 10 {
				s1.playerStates[whichPlayer].pos -= 10
			}
			if s1.playerStates[whichPlayer].tosses == 3 {
				s1.playerStates[whichPlayer].score += s1.playerStates[whichPlayer].pos
			}
			wc1 := checkState(s1)
			out.wins[0] += wc1.wins[0]
			out.wins[1] += wc1.wins[1]
		}
		m[sOrig] = out
		return out
	}

}

func mainX() {

	fmt.Println("Hello")
	m = make(map[State]WinCount)

	var p [2]PlayerState
	p[0] = PlayerState{9, 0, 0}
	p[1] = PlayerState{6, 0, 0}
	st := State{p, true}
	wc := checkState(st)

	fmt.Println(wc)
}
