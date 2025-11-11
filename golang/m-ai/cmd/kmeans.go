package cmd

import (
	"fmt"
	"log"
	"log/slog"
	helpers "mai"
	"math/rand"
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

func kmeans() {
	slog.Info("Knn means algorithm")

	dir, err := os.Getwd()
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(dir)

	filePath := dir + "/../../data/example1.csv"

	//slog.Info("File path:", "value", filePath)

	newPoint := []float64{18, 72}
	slog.Info("----------------------------------")
	slog.Info("New point to classify:", "value", newPoint)
	slog.Info("----------------------------------")

	data, err := helpers.ReadCsvFile(filePath)
	if err != nil {
		slog.Error("Error reading CSV file", "error", err)
		os.Exit(1)
	}

	sample := make([]Sample, 0)

	var s Sample

	slog.Info("----------------------------------")
	slog.Info("--- Data values ---")
	for i := 1; i < len(data); i++ {

		s.Features = helpers.GetArrayWithoutLabel(data[i])
		s.Distance = []float64{helpers.DistanceEuclidean(s.Features, newPoint)}
		s.Label = data[i][len(data[i])-1]

		slog.Info("Data", "value", s)
		sample = append(sample, s)
	}
	slog.Info("----------------------------------")

	slog.Info("----------------------------------")
	// Step-1: Choose the number of clusters K.
	K := 2
	slog.Info("Number of clusters K:", "value", K)
	slog.Info("----------------------------------")

	centroids := make([]Sample, 0)

	// Step-2: Select K random points as centroids.

	for i := 0; i < K; i++ {
		randomNumber := rand.Intn(len(sample))
		centroids = append(centroids, sample[randomNumber])
	}

	slog.Info("----------------------------------")
	slog.Info("Centroid: ", "value", centroids)
	slog.Info("----------------------------------")

	// Step-3: Assign each data point to the nearest centroid.
	x := 0
	for x < 3 {

		for i := 0; i < len(sample); i++ {
			minDistance := helpers.DistanceEuclidean(sample[i].Features, centroids[0].Features)
			sample[i].Label = centroids[0].Label

			for j := 1; j < len(centroids); j++ {
				distance := helpers.DistanceEuclidean(sample[i].Features, centroids[j].Features)
				if distance < minDistance {
					minDistance = distance
					sample[i].Label = centroids[j].Label
				}
			}
			slog.Info("Sample:", "Features", sample[i].Features, "Assigned Label", sample[i].Label)
		}

		// Step-4: Recalculate the centroids of the clusters.

		for i := 0; i < len(centroids); i++ {
			var clusterPoints [][]float64
			for j := 0; j < len(sample); j++ {
				if sample[j].Label == centroids[i].Label {
					clusterPoints = append(clusterPoints, sample[j].Features)
				}
			}
			slog.Info("Cluster points for centroid", "i", i, "value", clusterPoints)

			if len(clusterPoints) > 0 {
				newCentroid := make([]float64, len(clusterPoints[0]))
				for k := 0; k < len(clusterPoints[0]); k++ {
					var sum float64 = 0
					for m := 0; m < len(clusterPoints); m++ {
						sum += clusterPoints[m][k]
					}
					newCentroid[k] = sum / float64(len(clusterPoints))
				}
				centroids[i].Features = newCentroid
				slog.Info("New centroid for cluster", "i", i, "value", newCentroid)
			}
		}
		// Step-5: Repeat steps 3 and 4 until convergence.
		x++

	}

	// Step-6: Our model is ready.

	for i := 0; i < len(centroids); i++ {
		slog.Info("Final centroid: ", "n", i+1, "value", centroids[i])
	}
}
