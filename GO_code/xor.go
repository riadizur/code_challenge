package main

import (
	"fmt"
	"strconv"
)

func main() {
	var repeat bool = true
	for repeat {
		fmt.Print("Masukkan banyak angka: ")
		var n int
		fmt.Scan(&n)
		var a int = 0
		for i := 0; i < n; i++ {
			fmt.Print("Masukkan angka: ")
			var input string
			fmt.Scan(&input)
			num, err := strconv.Atoi(input)
			if err != nil {
				fmt.Println("Input tidak valid. Mohon masukkan bilangan bulat.")
				continue
			}
			a ^= num
		}
		fmt.Printf("Hasil XOR dari %d bilangan bulat tsb adalah: %d\n", n, a)
		var response string
		fmt.Print("Ulangi lagi? (yes/no): ")
		fmt.Scan(&response)
		if response != "yes" {
			repeat = false
		}
	}
	fmt.Println("END")
}