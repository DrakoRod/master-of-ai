package cmd

import (
	"fmt"
	"log"
	"log/slog"
	helpers "mai"
	"os"

	"github.com/spf13/cobra"
)

func init() {
	rootCmd.AddCommand(kmodesCmd)
}

var kmodesCmd = &cobra.Command{
	Use:   "kmodes",
	Short: "kmodes - is a k Modes algorithm to classify data points",
	Long: `
	Nearest neighbor algorithms are among the “simplest” supervised machine learning algorithms 
	and have been well studied in the field of pattern recognition over the last century.
	`,
	Run: func(cmd *cobra.Command, args []string) {
		knn()
	},
}

/*
Links
*/
type SampleCategory struct {
	Features []string
	Distance []float64
	Label    string
}

func kmodes() {

	slog.Info("kModes Alogorithm")

	dir, err := os.Getwd()
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(dir)

	filePath := dir + "/../../data/example1.csv"

	slog.Info("File path:", "value", filePath)

	newPoint := []float64{18, 72}
	slog.Info("New point to classify:", "value", newPoint)

	data, err := helpers.ReadCsvFile(filePath)
	if err != nil {
		slog.Error("Error reading CSV file", "error", err)
		os.Exit(1)
	}

	slog.Info("Data read from CSV file:", "value", data)

	// Step-1: Select the number K of the neighbors
	var k int = 3
	slog.Info("K value:", "value", k)

	// Step-2: Calculate the Euclidean distance of K number of neighbors

	samples := make([]Sample, 0)

	var s Sample

	for i := 1; i < len(data); i++ {

		slog.Info("Data row:", "value", data[i])

		s.Features = helpers.GetArrayWithoutLabel(data[i])
		s.Distance = []float64{helpers.DistanceEuclidean(s.Features, newPoint)}
		s.Label = data[i][len(data[i])-1]

		slog.Info("P:", "value", s)
		samples = append(samples, s)
	}

	// Step-3: Take the K nearest neighbors as per the calculated Euclidean distance.

	samples = orderSamplesByDistance(samples)

	slog.Info("********************************")
	for i := 0; i < len(samples); i++ {
		s := samples[i]
		slog.Info("Sample:", "Features", s.Features, "Distance", s.Distance, "Label", s.Label)
	}
	slog.Info("********************************")

	samples = samples[:k]

	slog.Info("K samples:", "value", samples)

	labelCount := make(map[string]int)

	for i := 0; i < len(samples[:k]); i++ {
		labelCount[samples[i].Label]++
	}

	slog.Info("Label count:", "value", labelCount)

	// Step-4: Among these k neighbors, count the number of the data points in each category.

	label, err := helpers.GetMax(labelCount)
	if err != nil {
		slog.Error("Error getting maximum label", "error", err)
		os.Exit(1)
	}

	slog.Info("The new point is classified as:", "value", label)

	// Step-5: Assign the new data points to that category for which the number of the neighbor is maximum.

	nPoint := Sample{
		Features: newPoint,
		Distance: []float64{0},
		Label:    label,
	}

	slog.Info("New point classified:", "value", nPoint)

	// Step-6: Our model is ready.
	slog.Info("Knn algorithm finished")

}
