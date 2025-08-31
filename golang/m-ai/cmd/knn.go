package cmd

import (
	"log/slog"
	helpers "mai"
	"os"

	"github.com/spf13/cobra"
)

func init() {
	rootCmd.AddCommand(knnCmd)
}

var knnCmd = &cobra.Command{
	Use:   "knn",
	Short: "Knn - is a k Nearest Neighbor algorithm to classify data points",
	Long: `
	Nearest neighbor algorithms are among the “simplest” supervised machine learning algorithms 
	and have been well studied in the field of pattern recognition over the last century.
	`,
	Run: func(cmd *cobra.Command, args []string) {
		knn()
	},
}

func knn() {
	slog.Info("Knn algorithm")

	d := helpers.DistanceEuclidean([]float64{4, 5, 6, 6}, []float64{4, 5, 6, 6})

	if d == -1 {
		slog.Error("Error calculating distance")
		os.Exit(1)
	}

	slog.Info("Euclidean Distance:", "value", d)

	/*
			Read CSV file
		slog.Info("Reading CSV file")
		slog.Info("Could you specify the path to the CSV file?")
		scanner := bufio.NewScanner(os.Stdin)

		for scanner.Scan() {
			filePath := scanner.Text()
			slog.Info("File path:", "value", filePath)

			data, err := helpers.ReadCsvFile(filePath)
			if err != nil {
				slog.Error("Error reading CSV file", "error", err)
				os.Exit(1)
			}

			slog.Info("Data read from CSV file:", "value", data)
		}*/
}
