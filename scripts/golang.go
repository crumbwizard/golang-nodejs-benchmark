package main

import ()

func main() {
	i, arr := 0, []int{1, 1}

	for i < 100_000 {
		var val int = 0

		for e := 0; e < len(arr); e++ {
			val += arr[e]
		}

		arr = append(arr, val)
		i += 1
	}
}