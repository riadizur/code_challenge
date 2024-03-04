package main

import (
	"fmt"
	"io"
	"os"
	"path/filepath"
	"time"
)

func main() {
	if len(os.Args) < 3 {
		fmt.Println("Usage: go run sync.go <source_directory> <destination_directory>")
		return
	}

	sourceDir := os.Args[1]
	destinationDir := os.Args[2]

	err := syncDirectories(sourceDir, destinationDir)
	if err != nil {
		fmt.Println("Error:", err)
	}
}

func syncDirectories(sourceDir, destinationDir string) error {
	// Initialize a map to keep track of file modification times
	fileModTimes := make(map[string]time.Time)

	// Start monitoring the source directory for changes
	err := filepath.Walk(sourceDir, func(path string, info os.FileInfo, err error) error {
		if err != nil {
			return err
		}

		// Calculate the corresponding destination path
		relPath, err := filepath.Rel(sourceDir, path)
		if err != nil {
			return err
		}
		destPath := filepath.Join(destinationDir, relPath)

		// Check if the file exists in the destination directory
		_, err = os.Stat(destPath)
		if err != nil {
			if os.IsNotExist(err) {
				// File doesn't exist in destination, so copy it
				err = copyFile(path, destPath)
				if err != nil {
					return err
				}
			} else {
				return err
			}
		}

		// Record the modification time of the file
		fileModTimes[path] = info.ModTime()

		return nil
	})
	if err != nil {
		return err
	}

	fmt.Println("Sync started. Press Ctrl+C to stop.")

	// Continuously monitor the source directory for changes
	for {
		err := filepath.Walk(sourceDir, func(path string, info os.FileInfo, err error) error {
			if err != nil {
				return err
			}

			// Check if the file has been modified since the last check
			modTime := info.ModTime()
			lastModTime, exists := fileModTimes[path]
			if !exists || modTime.After(lastModTime) {
				// File has been modified or is new, so copy it to destination
				relPath, err := filepath.Rel(sourceDir, path)
				if err != nil {
					return err
				}
				destPath := filepath.Join(destinationDir, relPath)

				err = copyFile(path, destPath)
				if err != nil {
					return err
				}

				// Update the modification time in the map
				fileModTimes[path] = modTime

				fmt.Println("Copied:", path)
			}

			return nil
		})
		if err != nil {
			fmt.Println("Error:", err)
		}

		// Sleep for 1 second before checking again
		time.Sleep(1 * time.Second)
	}
}

func copyFile(src, dest string) error {
	sourceFile, err := os.Open(src)
	if err != nil {
		return err
	}
	defer sourceFile.Close()

	destFile, err := os.Create(dest)
	if err != nil {
		return err
	}
	defer destFile.Close()

	_, err = io.Copy(destFile, sourceFile)
	if err != nil {
		return err
	}

	return nil
}
