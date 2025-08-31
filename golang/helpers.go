package helpers

import (
	"bytes"
	"io"
	"log/slog"
	"math"
	"os"
)

// Here you can add helper functions that can be used across the project

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
