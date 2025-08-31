package cmd

import (
	"fmt"

	"github.com/spf13/cobra"
)

func init() {
	rootCmd.AddCommand(versionCmd)
}

var versionCmd = &cobra.Command{
	Use:   "version",
	Short: "Print the version number of m-ai",
	Long:  `All software has versions. This is m-ai's`,
	Run: func(cmd *cobra.Command, args []string) {
		fmt.Println("m-ai v0.1.0")
	},
}
