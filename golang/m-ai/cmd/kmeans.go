package cmd

import (
	"log/slog"
	helpers "mai"
	"os"

	"github.com/spf13/cobra"
)

func init() {
	rootCmd.AddCommand(kmeansCmd)
}

var kmeansCmd = &cobra.Command{
	Use:   "kmeans",
	Short: "kmeans - is a k-means clustering algorithm to group data points",
	Long: `
	 is an unsupervised learning algorithm that groups data points into K clusters 
	 by assigning each data point to the cluster with the closest mean, or centroid.
	`,
	Run: func(cmd *cobra.Command, args []string) {
		kmeans()
	},
}

/*

https://www.iebschool.com/hub/algoritmo-k-means-que-es-y-como-funciona-big-data/


*/

func kmeans() {
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
