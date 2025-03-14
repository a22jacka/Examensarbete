package main

import (
	"database/sql"
	"fmt"
	"net/http"
	"strconv"

	_ "github.com/go-sql-driver/mysql"
	"github.com/labstack/echo/v4"
)

var db *sql.DB

func insertDbData(data WildFireEntry) {

}

func insertFireData(c echo.Context) error {
	return c.String(200, "ng :(")
}

func getDbData(limit, offset int) ([]WildFireEntry, error) {
	query := fmt.Sprintf("SELECT * FROM WildfireEntry LIMIT %d OFFSET %d;", limit, offset)
	rows, err := db.Query(query)
	if err != nil {
		return nil, err
	}
	defer rows.Close()
	var entries []WildFireEntry
	for rows.Next() {
		var entry WildFireEntry
		entry, err := ScanEntry(entry, rows)
		if err != nil {
			return nil, err
		}
		entries = append(entries, entry)
	}
	return entries, nil
}

func getFireData(c echo.Context) error {
	limit, err := strconv.Atoi(c.QueryParam("limit"))
	if err != nil {
		return c.String(http.StatusBadRequest, "Could not convert limit to int")
	}
	offset, err := strconv.Atoi(c.QueryParam("offset"))
	if err != nil {
		return c.String(http.StatusBadRequest, "Could not convert offset to int")
	}

	data, err := getDbData(limit, offset)
	if err != nil {
		panic(err)
	}

	// data -> json

	return c.JSON(200, data)
}

func main() {
	// echo setup
	e := echo.New()
	e.GET("/", func(c echo.Context) error {
		return c.String(http.StatusOK, "Hello, World!")
	})
	e.GET("/wildfires", getFireData)
	e.POST("/wildfires/addentry", insertFireData)

	// database setup
	var err error
	db, err = sql.Open("mysql", "root:exjobb@/wildfire")
	if err != nil {
		panic(err)
	}

	port := ":8080"
	e.Logger.Fatal(e.Start(port))
}
