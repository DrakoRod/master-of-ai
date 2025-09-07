package helpers

import (
	"bytes"
	"errors"
	"fmt"
	"io"
	"log/slog"
	"math"
	"os"
	"strconv"
)

/*
Function to calculate the Euclidean distance between two points
*/

func DistanceEuclidean(a, b []float64) float64 {

	var result float64
	// Calculate the Euclidean distance between two points

	if len(a) != len(b) {
		slog.Error("Points must have the same dimension")
		result = -1
		return result
	}

	max := len(a)

	var sum float64 = 0

	for i := 0; i < max; i++ {
		sum = sum + (a[i]-b[i])*(a[i]-b[i])
	}

	result = math.Sqrt(sum)

	return result
}

/*
Function to calculate the average of a slice of float32 numbers.
*/

func GetAvearage(data []float32) float32 {
	var sum float32 = 0
	for _, value := range data {
		sum += value
	}
	return sum /
		float32(len(data))
}

func GetArrayWithoutLabel(data []string) []float64 {
	// Function to return an array without the label

	result := make([]float64, 0)

	for i := 0; i < len(data)-1; i++ {
		var value float64

		slog.Info("Data[i]:", "value", data[i])
		value, err := strconv.ParseFloat(data[i], 64) // 64 for float64
		if err != nil {
			slog.Error("Error converting string to float64", "error", err)
			os.Exit(1)
		}
		result = append(result, value)
	}

	return result
}

/*
Function to read a CSV file and return the data as a slice of string slices
*/
func ReadCsvFile(filePath string) ([][]string, error) {
	file, err := os.Open(filePath)
	if err != nil {
		slog.Error("Error opening file", "error", err)
		return nil, err
	}
	defer file.Close()

	var data [][]string

	buf := new(bytes.Buffer)
	_, err = io.Copy(buf, file)
	if err != nil {
		slog.Error("Error reading file", "error", err)
		return nil, err
	}

	lines := bytes.Split(buf.Bytes(), []byte{'\n'})
	for _, line := range lines {
		fields := bytes.Split(line, []byte{','})
		var strFields []string
		for _, field := range fields {
			strFields = append(strFields, string(field))
		}
		data = append(data, strFields)
	}

	return data, nil
}

func GetMax(m map[string]int) (string, error) {
	// Handle empty map case
	if len(m) == 0 {
		fmt.Println("Map is empty, no maximum value.")
		return "", errors.New("empty map")
	}

	// Initialize maxVal with the value of the first element
	var labelResult string
	var maxVal int
	for _, v := range m {
		maxVal = v // Assign the first value to maxVal
		break      // Exit after assigning the first value
	}

	// Iterate and find the maximum
	for label, v := range m {
		if v > maxVal {
			labelResult = label
			maxVal = v
		}
	}
	return labelResult, nil
}
